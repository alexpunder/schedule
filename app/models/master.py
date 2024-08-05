from sqlalchemy.orm import relationship

from app.models.base import ClientMasterBase


class Master(ClientMasterBase):

    work = relationship('Work', back_populates='master')
