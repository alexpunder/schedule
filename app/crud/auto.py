from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import BaseCRUD
from app.models import Auto
from app.schemas import AutoExtendDB


class AutoCRUD(BaseCRUD):

    async def get_all_auto_from_db(
        self,
        session: AsyncSession,
    ):
        auto = await session.execute(
            select(self.model)
            .options(
                selectinload(
                    self.model.client
                )
            )
        )
        return auto.scalars().all()

    async def get_auto_by_id(
        self,
        auto_id: int,
        session: AsyncSession,
    ):
        auto = await session.execute(
            select(self.model)
            .where(
                self.model.id == auto_id
            )
            .options(
                selectinload(
                    self.model.client
                )
            )
        )
        return auto.scalars().first()


auto_crud = AutoCRUD(model=Auto, db_schema=AutoExtendDB)
