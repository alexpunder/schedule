from sqlalchemy import Column, String, Integer, Date, Time, ForeignKey

from app.core.db import Base


class Reservation(Base):
    dt_to_reserve = Column(Date)
    time_from_reserve = Column(Time)
    time_to_reserve = Column(Time)
    description = Column(String(255), nullable=False)
    work_order = Column(Integer, ForeignKey('workorder.id'), nullable=True)
    car_post = Column(Integer, ForeignKey('carpost.id'))
