from sqlalchemy import Column, String, Boolean, Time

from app.core.db import Base
from app.core.constants import (
    DEFAULT_BEGIN_TIME, DEFAULT_END_TIME
)


class CarPost(Base):
    is_active = Column(Boolean, default=True)
    name = Column(String(255), unique=True, nullable=False)
    time_to_begin = Column(Time, default=DEFAULT_BEGIN_TIME)
    time_to_end = Column(Time, default=DEFAULT_END_TIME)
