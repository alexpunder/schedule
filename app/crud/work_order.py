from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud import BaseCRUD
from app.models import Client, Work, WorkOrder
from app.schemas import WorkOrderDB
from app.api.validations.work_order import check_work_order_exist_and_get_id


class WorkOrderCRUD(BaseCRUD):

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
            .options(
                selectinload(self.model.work)
                .selectinload(Work.masters)
            )
            .options(
                selectinload(self.model.reservation)
            )
        )
        return work_orders.scalars().all()

    async def get_work_order_by_id(
        self,
        work_order_id: int,
        session: AsyncSession,
    ):
        return await check_work_order_exist_and_get_id(
            model=self.model,
            work_order_id=work_order_id,
            session=session,
        )


work_order_crud = WorkOrderCRUD(model=WorkOrder, db_schema=WorkOrderDB)
