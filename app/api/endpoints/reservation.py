from typing import Optional
from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.reservation import (
    ReservationDB, ReservationCreate, ReservationUpdate, ReservationExtend
)
from app.crud.reservation import crud_reservation
from app.api.validations.work_order import (
    check_work_order_exist_and_get_it
)
from app.api.validations.reservation import (
    check_reservation_and_get_it
)
from app.api.validations.car_post import (
    check_car_post_exist_and_get_it
)


router = APIRouter()


@router.get(
    '/date-reservations',
    response_model=Optional[list[ReservationDB]]
)
async def get_day_reservations(
    date: date,
    session: AsyncSession = Depends(get_async_session)
):
    day_reservations = await crud_reservation.get_date_reservations(
        date, session
    )
    return day_reservations


@router.get(
    '/{reservation_id}',
    response_model=ReservationExtend
)
async def get_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    reservation = await check_reservation_and_get_it(
        reservation_id, session
    )
    work_order = await check_work_order_exist_and_get_it(
        reservation.work_order, session, exception=False
    )
    car_post = await check_car_post_exist_and_get_it(
        reservation.car_post, session
    )
    reservation.work_order = work_order
    reservation.car_post = car_post
    return reservation


@router.get(
    '/{car_post_id}/car-post-reservations',
    response_model=Optional[list[ReservationDB]]
)
async def get_all_car_post_reservations(
    date_data: date,
    car_post_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    car_post_reservations = (
        await crud_reservation.get_all_car_post_reservations(
            date=date_data, car_post=car_post_id, session=session
        )
    )
    return car_post_reservations


@router.post(
    '/',
    response_model=ReservationDB
)
async def create_reservation(
    reservation: ReservationCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_reservation = await crud_reservation.create_reservation(
        reservation, session
    )
    return new_reservation


@router.patch(
    '/{reservation_id}',
    response_model=ReservationDB
)
async def update_reservation(
    reservation_id: int,
    update_data: ReservationUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    reservation = await check_reservation_and_get_it(
        reservation_id, session
    )
    updated_reservation = await crud_reservation.update_reservation(
        reservation, update_data, session
    )
    return updated_reservation


@router.delete(
    '/{reservation_id}',
    response_model=ReservationDB
)
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    reservation = await check_reservation_and_get_it(
        reservation_id, session
    )
    deleted_reservation = await crud_reservation.delete(
        reservation, session
    )
    return deleted_reservation
