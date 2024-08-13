from sqlalchemy.orm import Mapped

from app.core.db import Base


class ClientMasterBase(Base):

    __abstract__ = True

    first_name: Mapped[str]
    last_name: Mapped[str]
