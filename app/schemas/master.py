from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas import WorkFromMaster


class MasterBase(BaseModel):
    first_name: str
    last_name: str


class MasterDB(MasterBase):
    id: int
    works: list['WorkFromMaster']


class MasterFromWork(MasterBase):
    id: int
