from config.base import create_db
from repository.database import create_tables
from repository.tables_repository import insert_from_mission_to_target
from repository.target_repository import find_targets


def seed():
    create_db()
    create_tables()
    if len(find_targets()) == 0:
        insert_from_mission_to_target()