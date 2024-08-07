from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.master import Master
    from app.models.work_order import WorkOrder


class Work(Base):
    title: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]

    work_order: Mapped[list['WorkOrder']] = relationship(
        back_populates='work',
        secondary='workorderwork'
    )
    masters: Mapped[list['Master']] = relationship(
        back_populates='works',
        secondary='masterwork'
    )
