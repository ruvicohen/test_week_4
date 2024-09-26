from sqlalchemy import text

from config.base import session_factory

query_create_tables = """create table if not exists Countries (
            country_id serial primary key,
            country_name varchar(100) unique not null
        );
        
        create table if not exists Cities (
            city_id serial primary key,
            city_name varchar(100) unique not null,
            country_id int not null,
            foreign key (country_id) references Countries(country_id)
        );
        
        create table if not exists Industries (
            industry_id serial primary key,
            industry_name varchar(255) unique not null
        );
        
        CREATE TABLE if not exists Locations (
            location_id SERIAL PRIMARY KEY,
            latitude NUMERIC(10, 6),
            longitude NUMERIC(10, 6),
            CONSTRAINT unique_location UNIQUE (latitude, longitude)
        );
        
        
        
        create table if not exists TargetTypes (
            target_type_id serial primary key,
            target_type_name varchar(255) unique not null
        );
        
        
        create table if not exists Targets (
            target_id serial primary key,
            priority VARCHAR(5),
            country_id int not null,
            city_id int not null,
            location_id int not null,
            target_type_id int,
            foreign key (country_id) references Countries(country_id),
            foreign key (city_id) references Cities(city_id),
            foreign key (location_id) references Locations(location_id),
            foreign key (target_type_id) references TargetTypes (target_type_id)
        );
        """

query_insert_from_mission_to_target = """
                INSERT INTO Countries (country_name)
                SELECT DISTINCT target_country
                FROM mission
                WHERE target_country IS NOT NULL
                ON CONFLICT (country_name) DO NOTHING;
                
                INSERT INTO Cities (city_name, country_id)
                SELECT DISTINCT
                    m.target_city,
                    c.country_id
                FROM mission m
                JOIN Countries c ON m.target_country = c.country_name
                WHERE m.target_city IS NOT NULL
                ON CONFLICT (city_name) DO NOTHING;
                
                INSERT INTO Industries (industry_name)
                SELECT DISTINCT target_industry
                FROM mission
                WHERE target_industry IS NOT NULL
                ON CONFLICT (industry_name) DO NOTHING;
                
                INSERT INTO Locations (latitude, longitude)
                SELECT DISTINCT
                    m.target_latitude::NUMERIC(10, 6),
                    m.target_longitude::NUMERIC(10, 6)
                FROM mission m
                WHERE m.target_latitude IS NOT NULL 
                    AND m.target_longitude IS NOT NULL
                ON CONFLICT (latitude, longitude) DO NOTHING;
                
                INSERT INTO TargetTypes (target_type_name)
                SELECT DISTINCT target_type
                FROM mission
                WHERE target_type IS NOT NULL
                ON CONFLICT (target_type_name) DO NOTHING;
                
                INSERT INTO Targets (priority, country_id, city_id, location_id, target_type_id, industry_id)
                SELECT DISTINCT
                    NULLIF(m.target_priority, ''),  
                    c.country_id,
                    ci.city_id,
                    l.location_id,
                    tt.target_type_id,
                    i.industry_id
                FROM mission m
                JOIN Countries c ON m.target_country = c.country_name
                JOIN Cities ci ON m.target_city = ci.city_name
                JOIN Locations l ON m.target_latitude = l.latitude AND m.target_longitude = l.longitude
                LEFT JOIN TargetTypes tt ON m.target_type = tt.target_type_name
                JOIN Industries i ON i.industry_name = m.target_industry
                WHERE NULLIF(m.target_priority, '') IS NOT NULL  
                ON CONFLICT DO NOTHING;
                                """

def create_tables_with_execute():
    with session_factory() as session:
        session.execute(text(query_create_tables))
        session.commit()


def insert_from_mission_to_target():
    with session_factory() as session:
        session.execute(text(query_insert_from_mission_to_target))
        session.commit()