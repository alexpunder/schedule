from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud import BaseCRUD
from app.models import Work
from app.schemas import WorkDB


class WorkCRUD(BaseCRUD):

    async def get_work_by_id(
        self,
        work_id: int,
        session: AsyncSession,
    ):
        work = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.masters)
            )
            .options(
                selectinload(self.model.work_order)
            )
            .where(
                self.model.id == work_id
            )
        )
        return work.scalars().first()

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
