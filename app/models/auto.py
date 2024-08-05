from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Auto(Base):
    vin_code: Mapped[str]
    mark: Mapped[str]
    model: Mapped[str]
    year: Mapped[int]
    mileage: Mapped[int]
    client_id: Mapped[int | None] = mapped_column(
        ForeignKey('client.id')
    )

    client: Mapped['Client'] = relationship(
        back_populates='auto'
    )
