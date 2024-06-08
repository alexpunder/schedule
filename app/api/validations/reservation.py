from typing import Optional
from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.reservation import ReservationDB
from app.crud.reservation import crud_reservation


async def check_reservation_and_get_it(
    reservation_id: int,
    session: AsyncSession
) -> Optional[ReservationDB]:
    reservation = await crud_reservation.get(
        reservation_id, session
    )

    if not reservation:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такого резерва не существует.'
        )

    return reservation
