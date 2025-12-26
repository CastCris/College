from begin.globals import Messages

from sqlalchemy import inspect, text
from sqlalchemy.orm import DeclarativeMeta
import re

from .crypt import *
from .session import session

##
FIELD_CIPHER = lambda model: [ i for i in model.__dict__.keys() if re.search("^cipher_.*", i) ] if model else []
FIELD_HASHED = lambda model: [ i for i in model.__dict__.keys() if re.search("^hashed_.*", i) ] if model else []
FIELD_PHASHED = lambda model: [ i for i in model.__dict__.keys() if re.search("^phashed_.*", i) ] if model else []
FIELD_DEFAULT = lambda model: [ i for i in model.__dict__.keys() if re.search("^DEFAULT_.*", i) ] if model else []

##
STMT_INSERT = lambda model, values: f" INSERT INTO \"{model.__tablename__}\" " + "(" + ', '.join([ '"' + str(i) + '"' for i in values ]) + ")"
STMT_VALUES = lambda parameters: " VALUES (" + ', '.join([ ':' + str(i) for i in parameters ]) + ") "

##
op_comp = {
    'GK5F415E22lt': lambda column, value: column < value,
    'lte': lambda column, value: column <= value,

    'gt': lambda column, value: column > value,
    'gte': lambda column, value: column >= value,

    'eq': lambda column, value: column == value,
    'ne': lambda column, value: column != value,
    'in': lambda column, value: column.in_(value)
}

op_comp_by_operator = {
    '<': '__lt',
    '<=': '__lte',

    '>': '__gt',
    '>=': '__gte',

    '==': '',
    '!=': '__ne'
}


##
def model_args_filter(model:object, *args, **kwargs)->dict:
    field_cipher = FIELD_CIPHER(model)
    field_hashed = FIELD_HASHED(model)
    field_phashed = FIELD_PHASHED(model)
    field_default = FIELD_DEFAULT(model)

    kwargs_copy = kwargs.copy()

    ##
    for i in field_cipher:
        dek_wrap = kwargs_copy.get("dek", None)
        if dek_wrap is None:
            break

        dek = dek_decrypt(dek_wrap)
        _, attr_name = i.split('cipher_')

        if not attr_name in kwargs_copy.keys() or i in kwargs_copy.keys():
            continue

        kwargs_copy[i] = clm_encrypt_dek(kwargs_copy[attr_name], dek)

    for i in field_hashed:
        _, attr_name = i.split('hashed_')

        if not attr_name in kwargs_copy.keys() or i in kwargs_copy.keys():
            continue

        kwargs_copy[i] = clm_encrypt_sha256(kwargs_copy[attr_name])

    for i in field_phashed:
        _, attr_name = i.split('phashed_')

        if not attr_name in kwargs_copy.keys() or i in kwargs_copy.keys():
            continue

        kwargs_copy[i] = clm_encrypt_phash(kwargs_copy[attr_name])

    for i in field_default:
        if not 'default_values' in args:
            break

        _, attr_name = i.split('DEFAULT_')
        if attr_name in kwargs_copy.keys():
            continue

        for j in field_cipher:
            if not re.search(f".*_{attr_name}$", j):
                continue

            kwargs_copy[attr_name] = model.__dict__[i]
            if callable(model.__dict__[i]): # Verifiy if default value is a function
                kwargs_copy[attr_name] = model.__dict__[i]()

            break

        for j in field_hashed:
            if not re.search(f".*_{attr_name}$", j):
                continue

            kwargs_copy[attr_name] = model.__dict__[i]
            if callable(model.__dict__[i]):
                kwargs_copy[attr_name] = model.__dict__[i]()

            break
        
        if not attr_name in model.__dict__.keys() or attr_name in kwargs_copy.keys():
            continue

        kwargs_copy[attr_name] = model.__dict__[i]
        if callable(model.__dict__[i]):
            kwargs_copy[attr_name] = model.__dict__[i]()


    ##
    for i in list(kwargs_copy.keys()):
        if i in model.__dict__.keys():
            continue

        del kwargs_copy[i]

    return kwargs_copy


def model_create(model:object, **kwargs)->object|None:
    try:
        kwargs_copy = kwargs.copy()
        if not "dek" in kwargs_copy.keys() and "dek" in model.__dict__.keys():
            kwargs_copy["dek"] = dek_encrypt(dek_generate())

        ##
        print('kwargs_copy: ', kwargs_copy)
        model_args = model_args_filter(model, 'default_values', **kwargs_copy)
        print('model_args: ', model_args)
        instance = model(**model_args)

        return instance

    except Exception as e:
        Messages.Error.print('model_create', e)
        session.rollback()

        return None

def model_create_SQL(model:object, **kwargs)->dict|None:
    try:
        kwargs_copy = kwargs.copy()
        if not "dek" in kwargs_copy.keys() and "dek" in model.__dict__.keys():
            kwargs_copy["dek"] = dek_encrypt(dek_generate())

        ##
        print('kwargs_copy: ', kwargs_copy)
        model_args = model_args_filter(model, 'default_values', **kwargs_copy)
        print('model_args: ', model_args)

        INSERT = STMT_INSERT(model, model_args)
        VALUES = STMT_VALUES(list(model_args.keys()))
        STATEMENT = INSERT + VALUES

        print('stmt: ', STATEMENT)

        args = {
            'stmt': text(STATEMENT),
            'model_args': model_args
        }

        return args

    except Exception as e:
        Messages.Error.print('model_create_SQL', e)
        session.rollback()

        return None


def model_from_name(table_name:str)->object | None:
    from .session import Base, metadata

    ##
    try:
        table = metadata.tables.get(table_name, None)
        for i in metadata.tables.keys():
            if table_name:
                break

            if table_name.lower() == i.lower() :
                table = metadata.tables[i]
                break

        for i in Base.registry.mappers:
            if i.local_table.name == table.name:
                return i.class_

        return table

    except Exception as e:
        Messages.Error.print('model_from_name', e)
        session.rollback()

        return None

def model_from_tuple(model:DeclarativeMeta, attr:tuple)->DeclarativeMeta:
    try:
        kwargs = {
            column.name: value 
            for column, value in zip(model.__table__.columns, attr)
        }
        # print('model_from_tuple: ', kwargs)

        return model(**kwargs)

    except Exception as e:
        Messages.Error.print('model_from_name', e)

def model_get_PK(model:object)->list:
    return model.__table__.primary_key.columns.keys()

def model_is_mapped(model:object)->bool:
    return hasattr(model, '__tablename__')

# instance
def instance_update(instance:object, **kwargs)->None:
    try:
        model = type(instance)
        model_args = model_args_filter(model, **kwargs, dek=getattr(instance, "dek", None))

        for i in model_args.keys():
            setattr(instance, i, model_args[i])

        session.commit()

    except Exception as e:
        Messages.Error.print('model_update', e)
        session.rollback()

def instance_get(instance:object, *args)->tuple|None:
    try:
        model = type(instance)

        field_cipher = FIELD_CIPHER(model)
        field_hashed = FIELD_HASHED(model)
        
        #
        values = []

        for i in args:
            dek_wrap = getattr(instance, "dek", None)
            dek = dek_decrypt(dek_wrap) if not dek_wrap is None else None

            value = getattr(instance, i, None)
            if value is None:
                continue

            if not dek is None and i in field_cipher:
                values.append(clm_decrypt_dek(value, dek))
                continue

            values.append(value)

        if not len(values):
            values = [ None ]

        return tuple(values)

    except Exception as e:
        Messages.Error.print("model_get", e)

        return None

def instane_unwrap(instance:object)->dict|None:
    try:
        model = type(instance)

        field_cipher = FIELD_CIPHER(model)
        field_hashed = FIELD_HASHED(model)

        instance_unwrap = {}

        #
        for i in instance.__dict__.keys():
            if i == '_sa_instance_state' or i == 'dek':
                continue

            key_name = i if not i in field_cipher else i.split('cipher_')[1]
            instance_unwrap[key_name] = model_get(instance, i)[0]

        return instance_unwrap

    except Exception as e:
        Messages.Error.print('model_unwrap', e)
        session.rollback()

        return None

def instance_get_columns_value(instance:DeclarativeMeta)->dict:
    columns_value = {}

    field_hashed = FIELD_HASHED(type(instance))
    field_cipher = FIELD_CIPHER(type(instance))

    for i in mapper.columns:
        name = i.key
        if name in field_hashed:
            continue

        attr_name = name
        if name.startswith('cipher_'):
            _, attr_name = name.split('cipher_')
        
        value = model_get(instance, name)[0]

        columns_value[attr_name] = value

    return columns_value


def model_get_columns(model:DeclarativeMeta)->tuple:
    columns = [ i for i in model.__table__.columns]
    return tuple(columns)

def model_get_columns_name(model:DeclarativeMeta)->tuple:
    columns = model_get_columns(model)

    #
    field_cipher = FIELD_CIPHER(model)
    field_hashed = FIELD_HASHED(model)

    columns_name = []
    columns_name_set = set()

    for i in columns:
        name = i.name
        attr_name = name

        if name.startswith('cipher_'):
            _, attr_name = name.split('cipher_')

        if name.startswith('hashed_'):
            _, attr_name = name.split('hashed_')

        if attr_name in columns_name_set:
            continue

        columns_name.append(attr_name)
        columns_name_set.add(attr_name)

    return tuple(columns_name)

def model_get_columns_type(model:DeclarativeMeta)->dict:
    columns = model_get_columns(model)
    
    columns_type = {}
    columns_type_set = set()

    for i in columns:
        name, python_type = i.name, i.type.python_type
        attr_name = name

        if name.startswith('cipher_'):
            _, attr_name = name.split('cipher_')

        if name.startswith('hashed_'):
            _, attr_name = name.split('hashed_')

        if attr_name in columns_type_set:
            continue
        
        columns_type[attr_name] = python_type
        columns_type_set.add(attr_name)

    return columns_type
