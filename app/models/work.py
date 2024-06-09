from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class Work(Base):
    title = Column(String(255))
    price = Column(Integer)
    quantity = Column(Integer)
    master_id = Column(Integer, ForeignKey('master.id'))
    master = relationship('Master', back_populates='works')
    work_order_id = Column(Integer, ForeignKey('workorder.id'))
    work_order = relationship('WorkOrder', back_populates='works')
