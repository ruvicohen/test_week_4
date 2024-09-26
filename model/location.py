from sqlalchemy import Column, Integer, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from base import Base

class Location(Base):
    __tablename__ = 'locations'
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float(precision=8), nullable=False)
    longitude = Column(Float(precision=8), nullable=False)

    targets = relationship('Target', back_populates='location')

    __table_args__ = (UniqueConstraint('latitude', 'longitude', name='unique_location'),)
