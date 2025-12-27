from sqlalchemy import MetaData, text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

##
def sqlite_database_create(engine:object)->list:
    with open('./database/casts/schema_sqlite.sql', 'r') as file:
        sql = file.read()

    with engine.connect() as connection:
        for i in sql.split(';'):
            connection.execute(text(i))

        connection.commit()

    metadata = MetaData()
    metadata.reflect(bind=engine)

    Base = declarative_base(metadata=metadata)
    return Base, metadata

def postgres_database_create(engine:object)->list:
    with open('./database/casts/schema_postgres.sql', 'r') as file:
        sql = file.read()

    with engine.connect() as connection:
        connection.execute(text(sql))
        connection.commit()

    metadata = MetaData()
    metadata.reflect(bind=engine)

    Base = declarative_base(metadata=metadata)
    return Base, metadata


def _database_drop_tables(engine:object)->None:
    metadata = MetaData()
    metadata.reflect(bind=engine)

    metadata.drop_all(engine)

# def _database_init(dbms:str, _database_create:object)->None:
def _database_init(dbms:str, _database_create:callable)->list:
    from begin.xtensions import os, time
    from begin.globals import Config

    ##
    global engine

    global Base
    global metadata

    global session

    ##
    url = f"{dbms}://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}/{Config.DB_DATABASE}"

    for _ in range(20):
        try:
            engine = create_engine(url, echo=True)

            _database_drop_tables(engine)
            Base, metadata = _database_create(engine)

            Session = sessionmaker(bind=engine)
            session = Session()

            break

        except:
            print('Try establish connection with database again...')
            time.sleep(2)

    return engine, Base, session

#
engine = Base = metadata = session = None

# run locally
# _database_init('sqlite', sqlite_database_create)
_database_init('postgresql', postgres_database_create)
