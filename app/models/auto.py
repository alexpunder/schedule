from sqlalchemy import Column, String, Integer

from app.core.db import Base


class Auto(Base):
    vin_code = Column(String(255))
    mark = Column(String(255))
    model = Column(String(255))
    year = Column(Integer)
    mileage = Column(Integer)
