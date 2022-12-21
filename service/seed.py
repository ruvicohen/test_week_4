from config.base import create_db
from repository.database import create_tables, drop_tables
from repository.mission_repository import load_missions_to_db_from_csv
from repository.tables_native_sql_repository import insert_from_mission_to_target
from repository.target_repository import find_targets


def seed():
    drop_tables()
    create_db()
    create_tables()
    if len(find_targets()) == 0:
        load_missions_to_db_from_csv()
        insert_from_mission_to_target()
