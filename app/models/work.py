from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.master import Master
    from app.models.work_order import WorkOrder


class Work(Base):
    title: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
    work_order_id: Mapped[int | None] = mapped_column(
        ForeignKey('workorder.id')
    )

    work_order: Mapped['WorkOrder'] = relationship(
        back_populates='work'
    )
    masters: Mapped[list['Master']] = relationship(
        back_populates='works',
        secondary='masterwork'
    )
