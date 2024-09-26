from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Country(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(100), unique=True, nullable=False)

    cities = relationship('City', back_populates='country')
    targets = relationship('Target', back_populates='country')