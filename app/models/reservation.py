from sqlalchemy import Column, String, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class Reservation(Base):
    dt_to_reserve = Column(Date)
    time_from_reserve = Column(Time)
    time_to_reserve = Column(Time)
    description = Column(String(255), nullable=False)
    car_post_id = Column(Integer, ForeignKey('carpost.id'))
    work_order_id = Column(Integer, ForeignKey('workorder.id'), nullable=True)

    car_post = relationship('CarPost', back_populates='reservation')
    work_order = relationship('WorkOrder', back_populates='reservation')
