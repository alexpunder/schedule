from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud import BaseCRUD
from app.models import Reservation
from app.schemas import ReservationDB
from app.api.validations.reservation import (
    check_reservation_exist_and_get_id,
    checking_correctness_car_post_date_time_reservation,
)


class ReservationCRUD(BaseCRUD):

    async def get_all_reservations(
        self,
        session: AsyncSession,
    ):
        reservations = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.work_order)
            )
            .options(
                selectinload(self.model.car_post)
            )
        )
        return reservations.scalars().all()

    async def get_reservations_by_id(
        self,
        reservation_id: int,
        session: AsyncSession,
    ):
        return await check_reservation_exist_and_get_id(
            model=self.model,
            reservation_id=reservation_id,
            session=session,
        )

    async def get_reservations_by_date(
        self,
        reservations_date: date,
        session: AsyncSession,
    ):
        reservations = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.work_order)
            )
            .options(
                selectinload(self.model.car_post)
            )
            .where(
                self.model.dt_to_reserve == reservations_date
            )
        )
        return reservations.scalars().all()

    async def create_reservation_by_date_time(
        obj_data, session
    ):
        reservation_data = obj_data.dict()
        await checking_correctness_car_post_date_time_reservation(
            **reservation_data
        )
        pass


reservation_crud = ReservationCRUD(model=Reservation, db_schema=ReservationDB)
