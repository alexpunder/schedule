from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.master import MasterDB, MasterCreate, MasterUpdate
from app.core.db import get_async_session
from app.crud.master import crud_master
from app.api.validations.master import check_master_exist_and_get_it


router = APIRouter()


@router.get(
    '/{master_id}',
    response_model=MasterDB
)
async def get_master(
    master_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    master = await check_master_exist_and_get_it(
        master_id, session
    )
    return master


@router.get(
    '/',
    response_model=list[MasterDB]
)
async def get_all_masters(
    session: AsyncSession = Depends(get_async_session)
):
    all_masters = await crud_master.get_all(
        session
    )
    return all_masters


@router.post(
    '/',
    response_model=MasterDB
)
async def create_master(
    master_data: MasterCreate,
    session: AsyncSession = Depends(get_async_session)
):
    created_master = await crud_master.create(
        master_data, session
    )
    return created_master


@router.patch(
    '/{master_id}',
    response_model=MasterDB
)
async def update_master(
    master_id: int,
    master_update_data: MasterUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    master = await check_master_exist_and_get_it(
        master_id, session
    )
    updated_master = await crud_master.update(
        master, master_update_data, session
    )
    return updated_master


@router.delete(
    '/{master_id}',
    response_model=MasterDB
)
async def delete_master(
    master_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    master = await check_master_exist_and_get_it(
        master_id, session
    )
    deleted_master = await crud_master.delete(
        master, session
    )
    return deleted_master
