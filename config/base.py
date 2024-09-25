from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('postgresql://postgres:1234@localhost/blockbuster_movies')
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

def create_db():
    if not database_exists(engine.url):
        create_database(engine.url)

def session_factory():
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)
    return _SessionFactory()