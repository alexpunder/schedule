from typing import TYPE_CHECKING
from datetime import datetime

from pydantic import BaseModel

if TYPE_CHECKING:
    from .client import ClientDB
    from .reservation import ReservationFromWorkOrderDB


class WorkOrderBase(BaseModel):
    dt_to_create: datetime
    description: str


class WorkOrderDB(WorkOrderBase):
    id: int
    reservation: list['ReservationFromWorkOrderDB']
    client: 'ClientDB'


class WorkOrderFromReservation(WorkOrderBase):
    id: int
