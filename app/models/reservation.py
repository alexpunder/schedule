from datetime import date, time
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.car_post import CarPost
    from app.models.work_order import WorkOrder


class Reservation(Base):
    dt_to_reserve: Mapped[date]
    time_from_reserve: Mapped[time]
    time_to_reserve: Mapped[time]
    description: Mapped[str]
    car_post_id: Mapped[int] = mapped_column(
        ForeignKey('carpost.id')
    )
    work_order_id: Mapped[int | None] = mapped_column(
        ForeignKey('workorder.id')
    )

    car_post: Mapped['CarPost'] = relationship(
        back_populates='reservation'
    )
    work_order: Mapped['WorkOrder'] = relationship(
        back_populates='reservation'
    )
