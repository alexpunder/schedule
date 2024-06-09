from sqlalchemy.orm import relationship

from app.models.base import ClientMasterBase


class Master(ClientMasterBase):
    works = relationship('Work', back_populates='master')
