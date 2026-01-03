from begin.globals import Messages
from sqlalchemy.orm import DeclarativeMeta

from .model import *
from .session import session

##
def session_SQL(stmt:str, **kwargs)->tuple[DeclarativeMeta] or None:
    from sqlalchemy import text

    ##
    try:
        values = model_args_filter(kwargs.get("values")) if "values" in kwargs.keys() else None
        result = session.execute(text(stmt), values)
        session.commit();

        return result

    except Exception as e:
        Messages.Error.print('session_query_SQL', e)
        return None


def session_insert(model:DeclarativeMeta, **kwargs)->DeclarativeMeta:
    try:
        instance = model_create(model, **kwargs)

        session.add(instance)
        session.commit()

        return instance

    except Exception as e:
        Messages.Error.print('session_insert', e)
        session.rollback()

        return None

def session_insert_SQL(model:DeclarativeMeta, **kwargs)->None:
    try:
        args = model_create_SQL(model, **kwargs)
        session.execute(args['stmt'], args['model_kwargs'])
        session.commit();

    except Exception as e:
        Messages.Error.print('session_insert_SQL', e)
        session.rollback()


def session_update(instances:tuple[DeclarativeMeta], **kwargs)->None:
    try:
        for i in instances:
            instance_update(i, **kwargs)

        session.commit()

    except Exception as e:
        session.rollback()
        Messages.Error.print('session_update', e)

def session_delete(instances:tuple[DeclarativeMeta])->None:
    try:
        for i in instances:
            session.delete(i)

        session.commit()
    except Exception as e:
        session.rollback()
        Messages.Error.print('session_delete', e)


def session_query(*columns, **kwargs)->tuple|None:
    from sqlalchemy.orm import deferred

    try:
        model = columns[0].class_ if not model_is_mapped(columns[0]) else columns[0]
        instances_get = ()
        filters = []

        #
        filter_args = model_kwargs_filter(model, **kwargs)

        for i in kwargs.keys():
            if i in filter_args.keys():
                continue

            column_name, op = i, 'eq'
            if '__' in i:
                column_name, op = i.split('__')

            if not column_name in model.__dict__.keys() or not op in op_comp.keys():
                continue

            filter_args[i] = kwargs[i]

        print('kwargs: ', kwargs)
        print('filter_args: ', filter_args)
        ##
        for i in filter_args.keys():
            op = None
            column_name = op_type = None

            column_name, op_type = i, 'eq'
            if '__' in i:
                column_name, op_type = i.split('__')

            if not op_type in op_comp.keys():
                continue

            #
            op = op_comp[op_type]
            column = getattr(model, column_name, None)
            print(column, filter_args[i])

            filters.append(op(column, filter_args[i]))

        instances_get = session.query(*columns) \
            .filter(*filters) \
            .all()

        return instances_get

    except Exception as e:
        Messages.Error.print('session_query', e) 

        return None

def session_query_SQL(model:DeclarativeMeta, stmt:str, **kwargs)->tuple[DeclarativeMeta]|None:
    try:
        result_row = session_SQL(stmt).all()
        result_orm = []
        for row in result_row:
            row_dict = row._mapping
            print(model_get_PK(model))
            pkModel = { column_name: row_dict[column_name] for column_name in model_get_PK(model) if column_name in row_dict.keys() }

            if not pkModel:
                result_orm.append(model(**row_dict))
                continue

            result_orm.append(session_query(model, **pkModel)[0])
        return result_orm

    except Exception as e:
        Messages.Error.print('session_query_SQL', e)
        session.rollback()

        return None


##
def get_model(model_name:str)->object|None:
    from .session import Base, metadata

    ##
    table = metadata.tables[model_name]
    # print('table: ', table, type(table))

    for i in Base.registry.mappers:
        if i.local_table.name == table.name:
            return i.class_

    return None
