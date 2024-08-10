from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import Work
from app.schemas import WorkDB


class WorkCRUD:

    def __init__(self, model):
        self.model = model

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
        works_orm = works.scalars().all()
        result = [
            WorkDB.model_validate(row, from_attributes=True)
            for row in works_orm
        ]
        return result


work_crud = WorkCRUD(Work)
