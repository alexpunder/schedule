from sqlalchemy import select

from app.crud.base import CRUDBase
from app.models import WorkOrder, Work


class CRUDWorkOrder(CRUDBase):

    @staticmethod
    async def get_linked_works(
        object_id,
        session
    ):
        db_objects = await session.execute(
            select(Work).where(
                Work.work_order_id == object_id
            )
        )
        return db_objects.scalars().all()


crud_work_order = CRUDWorkOrder(WorkOrder)
