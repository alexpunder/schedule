from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.work import WorkDB, WorkCreate, WorkUpdate
from app.core.db import get_async_session
from app.crud.work import crud_work
from app.api.validations.work_order import (
    check_work_order_exist_and_get_it
)
from app.api.validations.work import check_work_exist_and_get_it
from app.api.validations.master import check_master_exist_and_get_it

router = APIRouter()


@router.get(
    '/{work_id}',
    response_model=WorkDB
)
async def get_work(
    work_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    work = await check_work_exist_and_get_it(
        work_id, session
    )

    try:
        master = await check_master_exist_and_get_it(
            work.master
        )
    except Exception as error:
        master = 0
        print(f'Возникал ошибка: {error}')

    work_order = await check_work_order_exist_and_get_it(
        work.work_order_id, session
    )

    work.master = master
    work.work_order_id = work_order
    return work


@router.get(
    '/',
    response_model=list[WorkDB]
)
async def get_all_works(
    session: AsyncSession = Depends(get_async_session)
):
    all_works = await crud_work.get_all(
        session
    )
    return all_works


@router.post(
    '/',
    response_model=WorkDB
)
async def create_work(
    work: WorkCreate,
    session: AsyncSession = Depends(get_async_session)
):
    await check_work_order_exist_and_get_it(
        work.work_order_id, session, get_object=False
    )
    await check_master_exist_and_get_it(
        work.master, session
    )
    new_work = await crud_work.create(
        work, session
    )
    return new_work


@router.patch(
    '/{work_id}',
    response_model=WorkDB
)
async def update_work(
    work_id: int,
    update_data: WorkUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    work = await check_work_exist_and_get_it(
        work_id, session
    )
    updated_work = await crud_work.update(
        work, update_data, session
    )
    return updated_work


@router.delete(
    '/{work_id}',
    response_model=WorkDB
)
async def delete_work(
    work_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    work = await check_work_exist_and_get_it(
        work_id, session
    )
    deleted_work = await crud_work.delete(
        work, session
    )
    return deleted_work
