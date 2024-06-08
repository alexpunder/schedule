from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.work import (
    WorkDB
)
from app.schemas.work_order import (
    WorkOrderDB, WorkOrderCreate, WorkOrderUpdate
)
from app.core.db import get_async_session
from app.crud.work_order import crud_work_order
from app.api.validations.work_order import (
    check_work_order_exist_and_get_it
)

router = APIRouter()


@router.get(
    '/{order_id}',
    response_model=WorkOrderDB
)
async def get_order(
    order_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    order = await check_work_order_exist_and_get_it(
        order_id, session
    )
    return order


@router.get(
    '/{order_id}/linked-works',
    response_model=list[WorkDB]
)
async def get_all_works_from_work_order(
    order_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    linked_works = await crud_work_order.get_linked_works(
        order_id, session
    )
    return linked_works


@router.get(
    '/',
    response_model=list[WorkOrderDB]
)
async def get_all_orders(
    session: AsyncSession = Depends(get_async_session)
):
    all_orders = await crud_work_order.get_all(
        session
    )
    return all_orders


@router.post(
    '/',
    response_model=WorkOrderDB
)
async def create_order(
    order: WorkOrderCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_order = await crud_work_order.create(
        order, session
    )
    return new_order


@router.patch(
    '/{order_id}',
    response_model=WorkOrderDB
)
async def update_order(
    order_id: int,
    update_data: WorkOrderUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    order = await check_work_order_exist_and_get_it(
        order_id, session
    )
    updated_order = await crud_work_order.update(
        order, update_data, session
    )
    return updated_order


@router.delete(
    '/{order_id}',
    response_model=WorkOrderDB
)
async def delete_order(
    order_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    order = await check_work_order_exist_and_get_it(
        order_id, session
    )
    deleted_order = await crud_work_order.delete(
        order, session
    )
    return deleted_order
