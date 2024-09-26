from sqlalchemy import Column, Integer, String
from base import Base

class Industry(Base):
    __tablename__ = 'industries'
    industry_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String(100), unique=True, nullable=False)
