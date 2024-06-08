from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Client


class CRUDClient(CRUDBase):

    async def create(
        self,
        object,
        session: AsyncSession
    ):
        db_object = await super().create(object, session)
        object_in_data = object.dict()
        auto_id = object_in_data.get('auto_id', 'EMPTY')
        return db_object, auto_id


crud_client = CRUDClient(Client)
