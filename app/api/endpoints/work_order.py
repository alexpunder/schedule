from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import work_order_crud
from app.schemas import WorkOrderDB

router = APIRouter()


@router.get('/{work_order_id}', response_model=WorkOrderDB)
async def get_work_order_by_id(
    work_order_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    work_order = await work_order_crud.get_work_order_by_id(
        work_order_id=work_order_id,
        session=session,
    )
    return work_order


@router.get('/', response_model=list[WorkOrderDB])
async def get_all_work_orders(
    session: AsyncSession = Depends(get_async_session),
):
    work_orders = await work_order_crud.get_all_work_orders(
        session=session,
    )
    return work_orders
