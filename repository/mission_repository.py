from config.base import session_factory, engine
import pandas as pd


def load_missions_to_db_from_csv():
    with session_factory() as session:
        csv_file = 'assets/operations.csv'
        dtype_spec = {
            'Callsign': 'string',  # Example: column 7 with mixed types
            'Mission Type': 'string',  # Example: column 8
            'Takeoff Latitude': 'string',  # Example: column 11
            'Target ID': 'string',  # Example: column 13
            'High Explosives Weight in Pounds': 'string',  # Example: column 31
            'Incendiary Devices': 'string',  # Example: column 43
            'Incendiary Devices Type': 'string',  # Example: column 44
        }
        df = pd.read_csv(csv_file, dtype=dtype_spec, low_memory=False)
        df.to_sql('mission', engine, if_exists='append', index=False)

