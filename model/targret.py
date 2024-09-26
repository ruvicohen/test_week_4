from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    priority = Column(Integer)

    country_id = Column(Integer, ForeignKey('countries.country_id'), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.location_id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('target_types.target_type_id'))

    country = relationship('Country', back_populates='targets')
    city = relationship('City', back_populates='targets')
    location = relationship('Location', back_populates='targets')
    target_type = relationship('TargetType', back_populates='targets')
