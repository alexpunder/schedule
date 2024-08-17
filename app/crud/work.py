from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud import BaseCRUD
from app.models import Work
from app.schemas import WorkDB
from app.api.validations.work import check_work_exist_and_get_id


class WorkCRUD(BaseCRUD):

    async def get_work_by_id(
        self,
        work_id: int,
        session: AsyncSession,
    ):
        return await check_work_exist_and_get_id(
            model=self.model,
            work_id=work_id,
            session=session,
        )

    async def get_all_works_form_db(
        self,
        session: AsyncSession,
    ):
        works = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.masters)
            )
            .options(
                selectinload(self.model.work_order)
            )
        )
        return works.scalars().all()


work_crud = WorkCRUD(model=Work, db_schema=WorkDB)
