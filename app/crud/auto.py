from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import BaseCRUD
from app.models import Auto
from app.schemas import AutoExtendDB
from app.api.validations.auto import check_auto_exist_and_get_id


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
        return await check_auto_exist_and_get_id(
            model=self.model,
            auto_id=auto_id,
            session=session,
        )


auto_crud = AutoCRUD(model=Auto, db_schema=AutoExtendDB)
