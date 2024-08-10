from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.schemas import MasterDB
from app.models import Master


class MasterCRUD:

    def __init__(self, model):
        self.model = model

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
        masters_orm = masters.scalars().all()
        result = [
            MasterDB.model_validate(row, from_attributes=True)
            for row in masters_orm
        ]
        return result


master_crud = MasterCRUD(Master)
