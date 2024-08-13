from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud import BaseCRUD
from app.models import Reservation
from app.schemas import ReservationDB


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
        reservation = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.work_order)
            )
            .options(
                selectinload(self.model.car_post)
            )
            .where(
                self.model.id == reservation_id
            )
        )
        return reservation.scalars().first()

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


reservation_crud = ReservationCRUD(model=Reservation, db_schema=ReservationDB)
