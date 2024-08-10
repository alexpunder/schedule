from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from .master import MasterFromWork
    from .work_order import WorkOrderFromReservation


class WorkBase(BaseModel):
    title: str
    price: int
    quantity: int


class WorkDB(WorkBase):
    id: int
    work_order: list['WorkOrderFromReservation']
    masters: list['MasterFromWork']


class WorkFromMaster(WorkBase):
    id: int


class WorkFromWorkOrder(WorkBase):
    id: int
    masters: list['MasterFromWork']
