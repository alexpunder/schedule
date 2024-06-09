from datetime import date

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, and_, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Reservation
from app.api.validations.shared_func import (
    check_car_post_and_work_order_exists,
    checking_correctness_car_post_dt_time_reservation,
    # check_reservation_intersections
)
from app.schemas.reservation import ReservationDB


class CRUDReservation(CRUDBase):

    async def create_reservation(
        self,
        object,
        session: AsyncSession
    ) -> ReservationDB:
        object_in_data = object.dict()
        car_post_id = object_in_data.get('car_post')
        work_order_id = object_in_data.get('work_order')
        time_from_reserve = object_in_data.get('time_from_reserve')
        time_to_reserve = object_in_data.get('time_to_reserve')
        dt_to_reserve = object_in_data.get('dt_to_reserve')

        car_post, _ = await check_car_post_and_work_order_exists(
            car_post_id=car_post_id,
            work_order_id=work_order_id,
            session=session
        )

        await checking_correctness_car_post_dt_time_reservation(
            car_post, time_from_reserve, time_to_reserve, dt_to_reserve
        )

        # await check_reservation_intersections(
        #     **object_in_data, session=session
        # )

        db_object = self.model(**object_in_data)
        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def update_reservation(
        self,
        db_object,
        object_in,
        session: AsyncSession
    ):
        object_data = jsonable_encoder(db_object)
        update_data = object_in.dict(exclude_unset=True)

        await check_car_post_and_work_order_exists(
            car_post_id=update_data.get('car_post'),
            work_order_id=update_data.get('work_order'),
            session=session
        )

        for field in object_data:
            if field in update_data:
                setattr(db_object, field, update_data[field])

        session.add(db_object)
        await session.commit()
        await session.refresh(db_object)
        return db_object

    async def get_all_car_post_reservations(
        self,
        date: date,
        car_post: int,
        session: AsyncSession
    ):
        car_post_reservations = await session.execute(
            select(Reservation).where(
                Reservation.car_post == car_post,
                and_(
                    func.DATE(date) == func.DATE(Reservation.dt_to_reserve)
                )
            )
        )
        car_post_reservations = car_post_reservations.scalars().all()
        return car_post_reservations


crud_reservation = CRUDReservation(Reservation)
