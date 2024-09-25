from config.base import create_db
from repository.database import create_tables


def seed():
    create_db()
    create_tables()