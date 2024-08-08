from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import reservation_crud
from app.schemas import ReservationDB

router = APIRouter()


@router.get('/', response_model=list[ReservationDB])
async def get_all_reservations(
    session: AsyncSession = Depends(get_async_session)
):
    reservations = await reservation_crud.get_all_reservations(
        session=session
    )
    return reservations


@router.get('/by_date', response_model=list[ReservationDB])
async def get_reservations_by_date(
    reservations_date: date = Query(...),
    session: AsyncSession = Depends(get_async_session),
):
    reservations = await reservation_crud.get_reservations_by_date(
        reservations_date=reservations_date,
        session=session,
    )
    return reservations


@router.get('/{reservation_id}', response_model=ReservationDB)
async def get_reservation_by_id(
    reservation_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    reservation = await reservation_crud.get_reservations_by_id(
        reservation_id=reservation_id,
        session=session,
    )
    return reservation
