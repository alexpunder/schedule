from typing import TYPE_CHECKING
from datetime import date, time

from pydantic import BaseModel

if TYPE_CHECKING:
    from .work_order import WorkOrderFromReservation
    from .car_post import CarPostFromReservation


class ReservationBase(BaseModel):
    dt_to_reserve: date
    time_from_reserve: time
    time_to_reserve: time
    description: str


class ReservationDB(ReservationBase):
    id: int
    car_post: 'CarPostFromReservation'
    work_order: 'WorkOrderFromReservation'


class ReservationFromWorkOrderDB(ReservationBase):
    id: int
