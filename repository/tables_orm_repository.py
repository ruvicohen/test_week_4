from config.base import session_factory
from model import Country, City, Industry, Location, TargetType, Target, Mission  # Assuming these are your models

def insert_from_mission_to_target_with_orm():
    with session_factory() as session:
        try:
            # Insert into Countries
            distinct_countries = session.query(Mission.TargetCountry).distinct().filter(Mission.TargetCountry.isnot(None))
            for country in distinct_countries:
                country_obj = Country(country_name=country.TargetCountry)
                session.add(country_obj)
                session.commit()
                session.refresh(country_obj)

            # Insert into Cities
            distinct_cities = session.query(Mission.TargetCity, Country.id).distinct() \
                .join(Country, Mission.TargetCountry == Country.country_name) \
                .filter(Mission.TargetCity.isnot(None))
            for city, country_id in distinct_cities:
                city_obj = City(city_name=city, country_id=country_id)
                session.add(city_obj)
                session.commit()
                session.refresh(city_obj)

            # Insert into Industries
            distinct_industries = session.query(Mission.TargetIndustry).distinct().filter(Mission.TargetIndustry.isnot(None))
            for industry in distinct_industries:
                industry_obj = Industry(industry_name=industry.target_industry)
                session.add(industry_obj)
                session.commit()
                session.refresh(industry_obj)

            # Insert into Locations
            distinct_locations = session.query(Mission.TargetLatitude, Mission.TargetLongitude).distinct() \
                .filter(Mission.TargetLatitude.isnot(None), Mission.TargetLongitude.isnot(None))
            for lat, lon in distinct_locations:
                location_obj = Location(latitude=lat, longitude=lon)
                session.add(location_obj)
                session.commit()
                session.refresh(location_obj)

            # Insert into TargetTypes
            distinct_target_types = session.query(Mission.TargetType).distinct().filter(Mission.TargetType.isnot(None))
            for target_type in distinct_target_types:
                target_type_obj = TargetType(target_type_name=target_type)
                session.add(target_type_obj)
                session.commit()
                session.refresh(target_type_obj)

            # Insert into Targets
            distinct_targets = session.query(
                Mission.target_priority, Country.id, City.id, Location.id, TargetType.id, Industry.id
            ).distinct() \
                .join(Country, Mission.TargetCountry == Country.country_name) \
                .join(City, Mission.TargetCity == City.city_name) \
                .join(Location, (Mission.TargetLatitude == Location.latitude) & (Mission.TargetLongitude == Location.longitude)) \
                .outerjoin(TargetType, Mission.TargetType == TargetType.target_type_name) \
                .join(Industry, Mission.TargetIndustry == Industry.industry_name) \
                .filter(Mission.TargetPriority.isnot(None))

            for priority, country_id, city_id, location_id, target_type_id, industry_id in distinct_targets:
                target_obj = Target(
                    priority=priority,
                    country_id=country_id,
                    city_id=city_id,
                    location_id=location_id,
                    target_type_id=target_type_id,
                    industry_id=industry_id
                )
                session.add(target_obj)
                session.commit()
                session.refresh(target_obj)

            # Commit all inserts
            session.commit()
        except Exception as e:
            #session.rollback()
            print(f"Error occurred: {e}")