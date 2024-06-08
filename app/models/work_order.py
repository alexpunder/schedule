from datetime import datetime as dt

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

from app.core.db import Base


class WorkOrder(Base):
    dt_to_create = Column(DateTime, default=dt.now)
    description = Column(String(255))
    works = relationship('Work', back_populates='work_order')
