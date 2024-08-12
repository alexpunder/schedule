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

    async def get_validated_auto_model(
        self,
        auto: Auto,
    ):
        return AutoExtendDB.model_validate(
            auto, from_attributes=True
        )

    async def get_all_validated_auto_model(
        self,
        auto: list[Auto],
    ):
        return [
            AutoExtendDB.model_validate(row, from_attributes=True)
            for row in auto
        ]

    async def create_auto_from_client(
        self,
        auto_data,
        session: AsyncSession,
    ):
        data = auto_data.dict()
        db_obj = self.model(**data)
        await self.add_commit_and_refresh_db(
            db_obj=db_obj,
            session=session,
        )
        result = await self.get_auto_by_id(
            auto_id=db_obj.id,
            session=session,
        )
        return result


auto_crud = AutoCRUD(Auto)
