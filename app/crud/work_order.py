from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models import WorkOrder, Client
from app.schemas import WorkOrderDB


class WorkOrderCRUD:

    def __init__(self, model):
        self.model = model

    async def get_all_work_orders(
        self,
        session: AsyncSession,
    ):
        work_orders = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.client)
                .selectinload(Client.auto)
            )
        )
        work_orders_orm = work_orders.scalars().all()
        result = [
            WorkOrderDB.model_validate(row, from_attributes=True)
            for row in work_orders_orm
        ]
        return result

    async def get_work_order_by_id(
        self,
        work_order_id: int,
        session: AsyncSession,
    ):
        work_order = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.client)
                .selectinload(Client.auto)
            )
            .where(
                self.model.id == work_order_id
            )
        )
        work_order_orm = work_order.scalars().first()
        result = WorkOrderDB.model_validate(
            work_order_orm,
            from_attributes=True
        )
        return result


work_order_crud = WorkOrderCRUD(WorkOrder)
