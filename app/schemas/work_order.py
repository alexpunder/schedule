from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas import ClientFromWorkOrder
    from app.schemas import ReservationFromWorkOrderDB
    from app.schemas import WorkFromWorkOrder


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
