from datetime import time
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.constants import DEFAULT_BEGIN_TIME, DEFAULT_END_TIME
from app.core.db import Base

if TYPE_CHECKING:
    from app.models import Reservation


class CarPost(Base):
    is_active: Mapped[bool] = mapped_column(default=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    time_to_begin: Mapped[time] = mapped_column(default=DEFAULT_BEGIN_TIME)
    time_to_end: Mapped[time] = mapped_column(default=DEFAULT_END_TIME)

    reservation: Mapped[list['Reservation']] = relationship(
        back_populates='car_post'
    )
