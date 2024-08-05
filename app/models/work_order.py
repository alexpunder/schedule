from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.work import Work
    from app.models.reservation import Reservation
    from app.models.client import Client


class WorkOrder(Base):
    dt_to_create: Mapped[datetime] = mapped_column(default=datetime.now)
    description: Mapped[str]
    client_id: Mapped[int | None] = mapped_column(ForeignKey('client.id'))

    work: Mapped['Work'] = relationship(
        back_populates='work_order'
    )
    reservation: Mapped['Reservation'] = relationship(
        back_populates='work_order'
    )
    client: Mapped['Client'] = relationship(
        back_populates='work_order'
    )
