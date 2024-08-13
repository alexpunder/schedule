from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud import BaseCRUD
from app.models import Client
from app.schemas import ClientDB


class ClientCRUD(BaseCRUD):

    def __init__(self, model, db_schema):
        self.model = model
        self.db_schema = db_schema

    async def get_client_by_id(
        self,
        client_id: int,
        session: AsyncSession,
    ):
        item_by_id = await session.execute(
            select(self.model).where(
                self.model.id == client_id
            )
            .options(selectinload(self.model.auto))
            .options(selectinload(Client.work_order))
        )
        return item_by_id.scalars().first()

    async def get_all_clients(
        self,
        session: AsyncSession,
    ):
        all_clients = await session.execute(
            select(self.model)
            .options(selectinload(self.model.auto))
            .options(selectinload(Client.work_order))
        )
        return all_clients.scalars().all()


client_crud = ClientCRUD(model=Client, db_schema=ClientDB)
