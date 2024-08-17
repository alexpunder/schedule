from http import HTTPStatus
from datetime import datetime, date, time, timedelta

from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Reservation
from app.api.validations import MODEL_OBJ_NOT_EXIST


async def check_reservation_exist_and_get_id(
    model: Reservation,
    reservation_id: int,
    session: AsyncSession,
) -> Reservation | None:
    reservation_obj = await session.execute(
        select(model)
        .options(
            selectinload(model.work_order)
        )
        .options(
            selectinload(model.car_post)
        )
        .where(
            model.id == reservation_id
        )
    )
    reservation = reservation_obj.scalars().first()

    if not reservation:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=MODEL_OBJ_NOT_EXIST.get(model.__name__),
        )

    return reservation


async def checking_correctness_car_post_date_time_reservation(
    car_post: int,
    time_from_reserve: time,
    time_to_reserve: time,
    dt_to_create: datetime
):
    DAYS_IN_PAST = 3
    current_date = date.today()
    check_date_difference = current_date - dt_to_create

    if check_date_difference > timedelta(days=DAYS_IN_PAST):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=(
                'Нельзя создавать резерв в прошлом более чем '
                f'{DAYS_IN_PAST} дней спустя.'
            ),
        )

    if not (
        car_post.time_to_begin <= time_from_reserve
        and car_post.time_to_end >= time_to_reserve
    ):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=(
                'Зарезервировать можно только в рамках времени работы поста: '
                f'с {car_post.time_to_begin} до {car_post.time_to_end}.'
            ),
        )
