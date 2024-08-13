from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas import (ClientFromWorkOrder, ReservationFromWorkOrderDB,
                             WorkFromWorkOrder)


class WorkOrderBase(BaseModel):
    dt_to_create: datetime
    description: str


class WorkOrderDB(WorkOrderBase):
    id: int
    reservation: list['ReservationFromWorkOrderDB']
    work: list['WorkFromWorkOrder']
    client: 'ClientFromWorkOrder'


class WorkOrderFromReservation(WorkOrderBase):
    id: int


class WorkOrderCreate(WorkOrderBase):
    client_id: int


class WorkOrderUpdate(WorkOrderCreate):
    pass
