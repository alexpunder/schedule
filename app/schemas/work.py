from typing import Union

from pydantic import BaseModel, PositiveInt

from app.schemas.master import MasterDB
from app.schemas.work_order import WorkOrderDB


class WorkBase(BaseModel):
    title: str
    price: PositiveInt
    quantity: PositiveInt
    master_id: int
    work_order_id: int

    class Config:
        str_min_length = 5


class WorkDB(WorkBase):
    id: int
    master_id: Union[MasterDB, int]
    work_order_id: Union[WorkOrderDB, int]


class WorkCreate(WorkBase):
    pass


class WorkUpdate(WorkBase):
    pass
