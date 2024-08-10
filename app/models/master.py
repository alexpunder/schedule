from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from app.models.base import ClientMasterBase

if TYPE_CHECKING:
    from app.models.work import Work


class Master(ClientMasterBase):

    works: Mapped[list['Work']] = relationship(
        back_populates='masters',
        secondary='masterwork'
    )
