from typing import TYPE_CHECKING
from datetime import date, time

from pydantic import BaseModel

if TYPE_CHECKING:
    from .work_order import WorkOrderFromReservation


class ReservationBase(BaseModel):
    dt_to_reserve: date
    time_from_reserve: time
    time_to_reserve: time
    description: str


class ReservationDB(ReservationBase):
    id: int
    work_order: 'WorkOrderFromReservation'


class ReservationFromWorkOrderDB(ReservationBase):
    id: int
