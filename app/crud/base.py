from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession


class BaseCRUD:

    def __init__(self, model, db_schema=None):
        self.model = model
        self.db_schema = db_schema

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

    async def get_validated_model_obj(
        self,
        orm_obj,
    ):
        return self.db_schema.model_validate(
            orm_obj, from_attributes=True
        )

    async def get_all_validated_model_objs(
        self,
        orm_obj,
    ):
        return [
            self.db_schema.model_validate(row, from_attributes=True)
            for row in orm_obj
        ]

    async def add_commit_and_refresh_db(
        self,
        db_obj,
        session: AsyncSession,
    ):
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
