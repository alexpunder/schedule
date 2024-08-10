from datetime import time
from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas import ReservationFromWorkOrderDB


class CarPostBase(BaseModel):
    is_active: bool
    name: str
    time_to_begin: time
    time_to_end: time


class CarPostDB(CarPostBase):
    id: int
    reservation: list['ReservationFromWorkOrderDB']
