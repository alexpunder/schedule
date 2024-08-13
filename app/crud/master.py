from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud import BaseCRUD
from app.models import Master
from app.schemas import MasterDB


class MasterCRUD(BaseCRUD):

    async def get_all_masters_form_db(
        self,
        session: AsyncSession,
    ):
        masters = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.works)
            )
        )
        return masters.scalars().all()

    async def get_master_by_id(
        self,
        master_id: int,
        session: AsyncSession,
    ):
        master = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.works)
            )
            .where(
                self.model.id == master_id
            )
        )
        return master.scalars().first()


master_crud = MasterCRUD(model=Master, db_schema=MasterDB)
