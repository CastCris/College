from begin.globals import Messages

from sqlalchemy import inspect, text
from sqlalchemy.orm import DeclarativeMeta
import re

from .crypt import *
from .session import session

##
FIELD_CIPHER = lambda model: [ i for i in vars(model) if re.search("^cipher_.*", i) ] if model else []
FIELD_HASHED = lambda model: [ i for i in vars(model) if re.search("^hashed_.*", i) ] if model else []
FIELD_PHASHED = lambda model: [ i for i in vars(model) if re.search("^phashed_.*", i) ] if model else []
FIELD_DEFAULT = lambda model: [ i for i in vars(model) if re.search("^DEFAULT_.*", i) ] if model else []

FIELD_METHOD_CREATE = lambda field_name: f"create_{field_name}"
FIELD_METHOD_UPDATE = lambda field_name: f"update_{field_name}"

FIELD_METHOD_EMPTY = lambda *args, **kwargs: None

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
def model_kwargs_filter(model:DeclarativeMeta, *args, **kwargs)->dict:
    field_cipher = FIELD_CIPHER(model)
    field_hashed = FIELD_HASHED(model)
    field_phashed = FIELD_PHASHED(model)
    field_default = FIELD_DEFAULT(model)

    kwargs_copy = kwargs.copy()

    default_values = 'default_values' in args

    ##
    for i in field_cipher:
        dek_wrap = kwargs_copy.get("dek", None)
        if dek_wrap is None:
            break

        dek = dek_decrypt(dek_wrap)
        _, attr_name = i.split('cipher_')

        # if not attr_name in kwargs_copy.keys() or i in kwargs_copy.keys():
        if not kwargs_copy.get(attr_name) or kwargs_copy.get(i):
            continue

        kwargs_copy[i] = clm_encrypt_dek(kwargs_copy[attr_name], dek)

    for i in field_hashed:
        _, attr_name = i.split('hashed_')

        # if not attr_name in kwargs_copy.keys() or i in kwargs_copy.keys():
        if not kwargs_copy.get(attr_name) or kwargs_copy.get(i):
            continue

        kwargs_copy[i] = clm_encrypt_sha256(kwargs_copy[attr_name])

    for i in field_phashed:
        _, attr_name = i.split('phashed_')

        # if not attr_name in kwargs_copy.keys() or i in kwargs_copy.keys():
        if not kwargs_copy.get(attr_name) or kwargs_copy.get(i):
            continue

        kwargs_copy[i] = clm_encrypt_phash(kwargs_copy[attr_name])

    for i in field_default:
        if not default_values:
            break

        _, attr_name = i.split('DEFAULT_')
        if kwargs_copy.get(attr_name):
            continue

        for j in field_cipher:
            if not re.search(f".*_{attr_name}$", j):
                continue

            # kwargs_copy[attr_name] = model.__dict__[i]
            kwargs_copy[attr_name] = getattr(model, i)
            if callable(model.__dict__[i]): # Verifiy if default value is a function
                # kwargs_copy[attr_name] = model.__dict__[i]()
                kwargs_copy[attr_name] = getattr(model, i)()

            break

        for j in field_hashed:
            if not re.search(f".*_{attr_name}$", j):
                continue

            # kwargs_copy[attr_name] = model.__dict__[i]
            kwargs_copy[attr_name] = getattr(model, i)
            if callable(model.__dict__[i]):
                # kwargs_copy[attr_name] = model.__dict__[i]()
                kwargs_copy[attr_name] = getattr(model, i)()

            break
        
        print('model_kwargs_filter: ', model, attr_name, kwargs_copy.get(attr_name))
        # if not attr_name in model.__dict__.keys() or attr_name in kwargs_copy.keys():
        # if not attr_name in model.__dict__.keys():
        if not hasattr(model, attr_name):
            continue

        kwargs_copy[attr_name] = getattr(model, i)
        if callable(model.__dict__[i]):
            # kwargs_copy[attr_name] = model.__dict__[i]()
            kwargs_copy[attr_name] = getattr(model, i)()


    ##
    for i in list(kwargs_copy.keys()):
        # if i in model.__dict__.keys():
        if hasattr(model, i):
            continue

        del kwargs_copy[i]

    return kwargs_copy

def model_args_filter(model:DeclarativeMeta, *args)->list[str]:
    field_cipher = FIELD_CIPHER(model)
    field_hashed = FIELD_HASHED(model)
    field_phashed = FIELD_PHASHED(model)

    no_cipher = 'no_cipher' in args
    no_hashed = 'no_hashed' in args
    no_phashed = 'no_phashed' in args

    ##
    args_filtered = []
    for attr_name in args:
        attr_cipher = 'cipher_' + attr_name
        attr_hashed = 'hashed_' + attr_name
        attr_phashed = 'phashed_' + attr_name

        if attr_cipher in field_cipher and not no_cipher:
            args_filtered.append(attr_cipher)
        
        if attr_hashed in field_hashed and not no_hashed:
            args_filtered.append(attr_hasehd)

        if attr_phashed in field_phashed and not no_phashed:
            args_filtered.append(attr_phashed)

        if not getattr(model, attr_name, None) is None:
            args_filtered.append(attr_name)

    return args_filtered


## Model create
def model_create(model:DeclarativeMeta, **kwargs)->object|None:
    try:
        kwargs_copy = kwargs.copy()
        # if not "dek" in kwargs_copy.keys() and "dek" in model.__dict__.keys():
        if not kwargs_copy.get("dek") and hasattr(model, "dek"):
            kwargs_copy["dek"] = dek_encrypt(dek_generate())

        ## Create Instance
        model_kwargs = model_kwargs_filter(model, 'default_values', **kwargs_copy)
        instance = model(**model_kwargs)

        print('kwargs_copy: ', kwargs_copy)
        print('model_kwargs: ', model_kwargs)

        ## Run create_ functions
        for attr_name, attr_value in kwargs.items():
            create_ = getattr(instance, FIELD_METHOD_CREATE(attr_name), FIELD_METHOD_EMPTY)
            create_(attr_value)

        return instance

    except Exception as e:
        Messages.Error.print('model_create', e)
        session.rollback()

        return None

def model_create_SQL(model:DeclarativeMeta, **kwargs)->dict|None:
    try:
        kwargs_copy = kwargs.copy()
        # if not "dek" in kwargs_copy.keys() and "dek" in model.__dict__.keys():
        if not kwargs_copy.get("dek") and hasattr(model, "dek"):
            kwargs_copy["dek"] = dek_encrypt(dek_generate())

        ##
        print('kwargs_copy: ', kwargs_copy)
        model_kwargs = model_kwargs_filter(model, 'default_values', **kwargs_copy)
        print('model_kwargs: ', model_kwargs)

        INSERT = STMT_INSERT(model, model_kwargs)
        VALUES = STMT_VALUES(list(model_kwargs.keys()))
        STATEMENT = INSERT + VALUES

        print('stmt: ', STATEMENT)

        args = {
            'stmt': text(STATEMENT),
            'model_kwargs': model_kwargs
        }

        return args

    except Exception as e:
        Messages.Error.print('model_create_SQL', e)
        session.rollback()

        return None


## Get model
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

def model_from_instance(instance:DeclarativeMeta):
    model = inspect(instance).mapper.class_
    return model

def mapper_from_instance(instance:DeclarativeMeta):
    mapper = inspect(instance).mapper
    return mapper

## Get model attributes
def model_get_PK(model:object)->list:
    return model.__table__.primary_key.columns.keys()

def model_is_mapped(model:object)->bool:
    return hasattr(model, '__tablename__')


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

# Instance methods
def instance_update(instance:DeclarativeMeta, **kwargs)->None:
    try:
        kwargs_copy = kwargs.copy()
        for attr_name, attr_value in list(kwargs_copy.items()):
            if instance_get(instance, attr_name)[0] == attr_value:
                del kwargs_copy[attr_name]

        model = type(instance)
        model_kwargs = model_kwargs_filter(model, **kwargs_copy, dek=getattr(instance, "dek", None))
        for attr_name, attr_value in model_kwargs.items():
            setattr(instance, attr_name, attr_value)

        ##
        for attr_name, attr_value in kwargs_copy.items():
            update_ = getattr(instance, FIELD_METHOD_UPDATE(attr_name), FIELD_METHOD_EMPTY)
            update_(attr_value)

        session.commit()

    except Exception as e:
        Messages.Error.print('instance_update', e)
        session.rollback()


## Instance get
def instance_get(instance:DeclarativeMeta, *args)->tuple|None:
    try:
        model = type(instance)

        field_cipher = FIELD_CIPHER(model)
        field_hashed = FIELD_HASHED(model)
        
        #
        args_filtered = model_args_filter(model, *args, 'no_hashed')
        print('args_filtered: ', args_filtered)

        values = []

        for i in args_filtered:
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
        Messages.Error.print("instance_get", e)

        return None

def instance_get_columns(instance:DeclarativeMeta)->tuple:
    mapper = mapper_from_instance(instance)
    return model_get_columns()

def instance_get_columns_name(instance:DeclarativeMeta)->tuple:
    mapper = mapper_from_instance(instance)
    return model_get_columns_name(mapper)

def instance_get_columns_type(instance:DeclarativeMeta)->tuple:
    mapper = model_from_instance(instance)
    return model_get_columns_type(mapper)

def instance_get_columns_value(instance:DeclarativeMeta)->dict:
    mapper = mapper_from_instance(instance)
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
        
        value = instance_get(instance, name)[0]

        columns_value[attr_name] = value

    return columns_value

def instane_unwrap(instance:DeclarativeMeta)->dict|None:
    try:
        model = type(instance)

        field_cipher = FIELD_CIPHER(model)
        field_hashed = FIELD_HASHED(model)

        instance_unwrap = {}

        #
        for i in vars(instance):
            if i == '_sa_instance_state' or i == 'dek':
                continue

            key_name = i if not i in field_cipher else i.split('cipher_')[1]
            instance_unwrap[key_name] = instance_get(instance, i)[0]

        return instance_unwrap

    except Exception as e:
        Messages.Error.print('model_unwrap', e)
        session.rollback()

        return None
