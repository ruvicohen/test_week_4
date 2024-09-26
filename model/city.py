from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.base import Base


class City(Base):
    __tablename__ = 'cities'

    city_id = Column(Integer, primary_key=True)
    city_name = Column(String(100), unique=True, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.country_id'), nullable=False)

    # Relationship to country
    country = relationship("Country", back_populates="cities", lazy="joined")
