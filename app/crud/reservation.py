from datetime import date

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import Reservation
from app.schemas import ReservationDB


class ReservationCRUD:

    def __init__(self, model):
        self.model = model

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
        reservation_orm = reservations.scalars().all()
        result = [
            ReservationDB.model_validate(row, from_attributes=True)
            for row in reservation_orm
        ]
        return result

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
        reservation_orm = reservation.scalars().first()
        result = ReservationDB.model_validate(
            reservation_orm,
            from_attributes=True,
        )
        return result

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
        reservations_orm = reservations.scalars().all()
        result = [
            ReservationDB.model_validate(row, from_attributes=True)
            for row in reservations_orm
        ]
        return result


reservation_crud = ReservationCRUD(Reservation)
