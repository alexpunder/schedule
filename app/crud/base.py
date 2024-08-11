from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseCRUD:

    def __init__(self, model):
        self.model = model

    async def get_obj_by_id(
        self,
        id_obj: int,
        session: AsyncSession,
    ):
        obj = await session.execute(
            select(self.model)
            .where(
                self.model.id == id_obj
            )
        )
        return obj.scalars().first()

    async def create_obj(
        self,
        data_obj,
        session: AsyncSession,
    ):
        data = data_obj.dict()
        db_obj = self.model(**data)
        await self.add_commit_and_refresh_db(
            db_obj=db_obj,
            session=session,
        )
        return db_obj

    async def update_obj(
        self,
        db_obj,
        update_data_obj,
        session: AsyncSession,
    ):
        encoded_obj = jsonable_encoder(db_obj)
        update_data = update_data_obj.dict(exclude_unset=True)

        for key in encoded_obj:
            if key in update_data:
                setattr(db_obj, key, update_data[key])

        await self.add_commit_and_refresh_db(
            db_obj=db_obj,
            session=session,
        )
        return db_obj

    async def delete_obj(
        self,
        obj,
        session: AsyncSession,
    ):
        await session.delete(obj)
        await session.commit()
        return obj

    async def add_commit_and_refresh_db(
        self,
        db_obj,
        session: AsyncSession,
    ):
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
