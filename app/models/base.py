from sqlalchemy import Column, String

from app.core.db import Base


class ClientMasterBase(Base):

    __abstract__ = True

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
