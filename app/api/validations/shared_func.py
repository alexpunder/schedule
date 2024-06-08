from http import HTTPStatus
from typing import Optional
from datetime import datetime, timedelta, time

from fastapi.exceptions import HTTPException
from sqlalchemy import select, and_, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Reservation
from app.api.validations.car_post import (
    check_car_post_exist_and_get_it
)
from app.api.validations.work_order import (
    check_work_order_exist_and_get_it
)


async def check_car_post_and_work_order_exists(
    car_post_id: int,
    work_order_id: Optional[int],
    session: AsyncSession
):
    car_post = await check_car_post_exist_and_get_it(
        car_post_id, session
    )

    if work_order_id is not None:
        work_order = await check_work_order_exist_and_get_it(
            work_order_id, session
        )
    else:
        work_order = None

    return car_post, work_order


async def checking_correctness_car_post_dt_time_reservation(
    car_post, time_from_reserve, time_to_reserve, dt_to_create
):
    DAYS_IN_PAST = 3
    current_dt_time = datetime.now()
    check_dt_difference = current_dt_time - dt_to_create

    if check_dt_difference > timedelta(days=DAYS_IN_PAST):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=(
                'Нельзя создавать резерв в прошлом более чем '
                f'{DAYS_IN_PAST} дней спустя.'
            )
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
            )
        )


# async def check_reservation_intersections(
#     *,
#     dt_to_create: datetime,
#     time_from_reserve: time,
#     time_to_reserve: time,
#     description: str,
#     work_order: Optional[int],
#     car_post: int,
#     session: AsyncSession
# ):
#     car_post_reservations = await session.execute(
#         select(Reservation).where(
#             Reservation.car_post == car_post,
#             and_(
#                 time_from_reserve <= Reservation.time_to_reserve,
#                 time_to_reserve >= Reservation.time_from_reserve
#             ),
#             and_(
#                 func.DATE(dt_to_create) == func.DATE(Reservation.dt_to_create)
#             )
#         )
#     )
#     # car_post_reservations = car_post_reservations.scalars().all()
#     # return car_post_reservations

#     if car_post_reservations:
#         raise HTTPException(
#             status_code=HTTPStatus.BAD_REQUEST,
#             detail=(
#                 'Нельзя бронировать поверх зарезервированного времени.'
#             )
#         )
