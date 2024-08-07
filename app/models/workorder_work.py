from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class WorkorderWork(Base):
    work_order: Mapped[int] = mapped_column(
        ForeignKey('workorder.id')
    )
    work: Mapped[int] = mapped_column(
        ForeignKey('work.id')
    )