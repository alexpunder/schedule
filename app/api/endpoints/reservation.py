from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import reservation_crud
from app.schemas import (
    ReservationDB, ReservationCreate, ReservationUpdate,
    ReservationFromWorkOrderDB,
)

router = APIRouter()


@router.get('/', response_model=list[ReservationDB])
async def get_all_reservations(
    session: AsyncSession = Depends(get_async_session)
):
    reservations = await reservation_crud.get_all_reservations(
        session=session,
    )
    return reservations


@router.get('/by_date', response_model=list[ReservationDB])
async def get_reservations_by_date(
    reservations_date: date = Query(...),
    session: AsyncSession = Depends(get_async_session),
):
    reservations_by_date = await reservation_crud.get_reservations_by_date(
        reservations_date=reservations_date,
        session=session,
    )
    return reservations_by_date


@router.get('/{reservation_id}', response_model=ReservationDB)
async def get_reservation_by_id(
    reservation_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    reservation_by_id = await reservation_crud.get_reservations_by_id(
        reservation_id=reservation_id,
        session=session,
    )
    return reservation_by_id


@router.post('/', response_model=ReservationDB)
async def create_reservation(
    reservation_data: ReservationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_reservation = await reservation_crud.create_obj(
        data_obj=reservation_data, session=session,
    )
    created_reservation = await reservation_crud.get_reservations_by_id(
        reservation_id=new_reservation.id, session=session,
    )
    return created_reservation


@router.patch('/{reservation_id}', response_model=ReservationDB)
async def update_reservation(
    reservation_id: int,
    update_data: ReservationUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    reservation = await reservation_crud.get_reservations_by_id(
        reservation_id=reservation_id, session=session,
    )
    updated_reservation = await reservation_crud.update_obj(
        db_obj=reservation,
        update_data_obj=update_data,
        session=session,
    )
    return updated_reservation


@router.delete('/{reservation_id}', response_model=ReservationFromWorkOrderDB)
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    reservation = await reservation_crud.get_reservations_by_id(
        reservation_id=reservation_id, session=session,
    )
    deleted_reservation = await reservation_crud.delete_obj(
        obj=reservation, session=session,
    )
    return deleted_reservation
