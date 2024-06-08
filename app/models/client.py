from sqlalchemy import Column, ForeignKey, Integer, String

from app.models.base import ClientMasterBase


class Client(ClientMasterBase):
    phone_number = Column(String(30), nullable=False)
    auto_id = Column(Integer, ForeignKey('auto.id'))
