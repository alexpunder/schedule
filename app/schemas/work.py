from typing import TYPE_CHECKING
from pydantic import BaseModel

if TYPE_CHECKING:
    from .master import MasterFromWork


class WorkBase(BaseModel):
    title: str
    price: int
    quantity: int


class WorkDB(WorkBase):
    id: int
    masters: list['MasterFromWork']


class WorkFromMaster(WorkBase):
    id: int
