from sqlalchemy import Column, Integer, Numeric, UniqueConstraint
from config.base import Base


class Location(Base):
    __tablename__ = 'locations'

    location_id = Column(Integer, primary_key=True)
    latitude = Column(Numeric(10, 6))
    longitude = Column(Numeric(10, 6))

    # Unique constraint for latitude and longitude
    __table_args__ = (
        UniqueConstraint('latitude', 'longitude', name='unique_location'),
    )