from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.client import Client
    from app.models.reservation import Reservation
    from app.models.work import Work


class WorkOrder(Base):
    dt_to_create: Mapped[datetime] = mapped_column(default=datetime.now)
    description: Mapped[str]
    client_id: Mapped[int | None] = mapped_column(ForeignKey('client.id'))

    work: Mapped[list['Work']] = relationship(
        back_populates='work_order',
        secondary='workorderwork'
    )
    reservation: Mapped[list['Reservation']] = relationship(
        back_populates='work_order'
    )
    client: Mapped['Client'] = relationship(
        back_populates='work_order'
    )
