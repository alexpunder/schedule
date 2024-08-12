from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas import MasterFromWork
    from app.schemas import WorkOrderFromReservation


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
