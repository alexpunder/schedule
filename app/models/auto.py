from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base

if TYPE_CHECKING:
    from app.models.client import Client


class Auto(Base):
    vin_code: Mapped[str]
    mark: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    mileage: Mapped[int]
    client_id: Mapped[int | None] = mapped_column(
        ForeignKey('client.id')
    )

    client: Mapped['Client'] = relationship(back_populates='auto')
