from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import work_order_crud
from app.schemas import (
    WorkOrderDB, WorkOrderFromReservation, WorkOrderCreate, WorkOrderUpdate,
)

router = APIRouter()


@router.get('/', response_model=list[WorkOrderDB])
async def get_all_work_orders(
    session: AsyncSession = Depends(get_async_session),
):
    work_orders = await work_order_crud.get_all_work_orders(
        session=session,
    )
    return work_orders


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


@router.post('/', response_model=WorkOrderDB)
async def create_work_order(
    work_order_data: WorkOrderCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_work_order = await work_order_crud.create_obj(
        data_obj=work_order_data, session=session,
    )
    created_work_order = await work_order_crud.get_work_order_by_id(
        work_order_id=new_work_order.id, session=session,
    )
    return created_work_order


@router.patch('/{work_order_id}', response_model=WorkOrderDB)
async def update_work_order(
    work_order_id: int,
    update_work_order_data: WorkOrderUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    work_order = await work_order_crud.get_work_order_by_id(
        work_order_id=work_order_id, session=session,
    )
    updated_work_order = await work_order_crud.update_obj(
        db_obj=work_order,
        update_data_obj=update_work_order_data,
        session=session,
    )
    return updated_work_order


@router.delete('/{work_order_id}', response_model=WorkOrderFromReservation)
async def delete_work_order(
    work_order_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    work_order = await work_order_crud.get_work_order_by_id(
        work_order_id=work_order_id, session=session,
    )
    deleted_work_order = await work_order_crud.delete_obj(
        obj=work_order, session=session,
    )
    return deleted_work_order
