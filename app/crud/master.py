from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud import BaseCRUD
from app.models import Master
from app.schemas import MasterDB
from app.api.validations.master import check_master_exist_and_get_id


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
        return await check_master_exist_and_get_id(
            model=self.model,
            master_id=master_id,
            session=session,
        )


master_crud = MasterCRUD(model=Master, db_schema=MasterDB)
