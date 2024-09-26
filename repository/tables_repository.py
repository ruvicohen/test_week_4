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
        
        create table if not exists Locations (
            location_id SERIAL PRIMARY KEY,
            latitude DECIMAL(10, 8),
            longitude DECIMAL(11, 8),
            CONSTRAINT unique_location UNIQUE (latitude, longitude)
        );
        
        
        create table if not exists TargetTypes (
            target_type_id serial primary key,
            target_type_name varchar(255) unique not null
        );
        
        
        create table if not exists Targets (
            target_id serial primary key,
            priority int,
            country_id int not null,
            city_id int not null,
            location_id int not null,
            target_type_id int,
            foreign key (country_id) references Countries(country_id),
            foreign key (city_id) references Cities(city_id),
            foreign key (location_id) references Locations(location_id),
            foreign key (target_type_id) references TargetTypes (target_type_id)
        );"""


def create_tables_with_execute():
    with session_factory() as session:
        query_result = session.execute(text(query_create_tables))
        return query_result.fetchone()
