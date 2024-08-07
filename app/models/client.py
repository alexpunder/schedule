from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from app.models.base import ClientMasterBase

if TYPE_CHECKING:
    from app.models.work_order import WorkOrder
    from app.models.auto import Auto


class Client(ClientMasterBase):
    phone_number: Mapped[str]

    work_order: Mapped[list['WorkOrder']] = relationship(
        back_populates='client'
    )
    auto: Mapped[list['Auto']] = relationship(
        back_populates='client'
    )
