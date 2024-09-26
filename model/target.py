from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base


class Target(Base):
    __tablename__ = 'targets'

    target_id = Column(Integer, primary_key=True)
    priority = Column(String(5))
    country_id = Column(Integer, ForeignKey('countries.country_id'), nullable=False)
    city_id = Column(Integer, ForeignKey('cities.city_id'), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.location_id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    industry_id = Column(Integer, ForeignKey('industries.industry_id'))

    # Relationships
    country = relationship("Country")
    city = relationship("City")
    location = relationship("Location")
    target_type = relationship("TargetType")
    industry = relationship("Industry")
