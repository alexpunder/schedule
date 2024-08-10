from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from app.schemas import ClientDB
from app.models import Client


class ClientCRUD:

    def __init__(self, model):
        self.model = model

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
        result_orm = item_by_id.scalars().first()
        result = ClientDB.model_validate(result_orm, from_attributes=True)
        return result

    async def get_all_clients(
        self,
        session: AsyncSession,
    ):
        all_clients = await session.execute(
            select(self.model)
            .options(selectinload(self.model.auto))
            .options(selectinload(Client.work_order))
        )
        result_orm = all_clients.scalars().all()
        result = [
            ClientDB.model_validate(row, from_attributes=True)
            for row in result_orm
        ]
        return result


client_crud = ClientCRUD(Client)
