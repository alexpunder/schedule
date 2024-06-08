from typing import Optional
from datetime import datetime, time, timedelta

from pydantic import BaseModel, Field

from app.schemas.car_post import CarPostDB
from app.schemas.work_order import WorkOrderDB


dt_format = '%Y-%m-%dT%H:%M'
time_format = '%H:%M'

DT_NOW = datetime.now().strftime(dt_format)
FROM_TIME = (
    datetime.now() + timedelta(minutes=10)
).time().strftime(time_format)
TO_TIME = (
    datetime.now() + timedelta(minutes=40)
).time().strftime(time_format)


class ReservationBase(BaseModel):
    dt_to_create: datetime = Field(..., example=DT_NOW)
    time_from_reserve: time = Field(..., example=FROM_TIME)
    time_to_reserve: time = Field(..., example=TO_TIME)
    description: str

    class Config:
        extra = 'forbid'
        str_min_length = 5


class ReservationDB(ReservationBase):
    work_order: Optional[int] = None
    car_post: int
    id: int

    class Config:
        from_attributes = True


class ReservationExtend(ReservationBase):
    work_order: Optional[WorkOrderDB] = None
    car_post: CarPostDB


class ReservationCreate(ReservationBase):
    work_order: Optional[int] = None
    car_post: int


class ReservationUpdate(ReservationCreate):
    pass
