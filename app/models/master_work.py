from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class MasterWork(Base):
    master_id: Mapped[int] = mapped_column(
        ForeignKey('master.id')
    )
    work_id: Mapped[int] = mapped_column(
        ForeignKey('work.id')
    )
