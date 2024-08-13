from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import master_crud
from app.schemas import MasterDB, MasterCreate, MasterUpdate

router = APIRouter()


@router.get('/', response_model=list[MasterDB])
async def get_all_masters(
    session: AsyncSession = Depends(get_async_session),
):
    masters = await master_crud.get_all_masters_form_db(
        session=session
    )
    return masters


@router.get('/{master_id}', response_model=MasterDB)
async def get_master_by_id(
    master_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    master = await master_crud.get_master_by_id(
        master_id=master_id,
        session=session,
    )
    return master


@router.post('/', response_model=MasterDB)
async def create_master(
    master_data: MasterCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_master = await master_crud.create_obj(
        data_obj=master_data, session=session,
    )
    created_master = await master_crud.get_master_by_id(
        master_id=new_master.id, session=session,
    )
    return created_master


@router.patch('/{master_id}', response_model=MasterDB)
async def update_master(
    master_id: int,
    update_master_data: MasterUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    master = await master_crud.get_master_by_id(
        master_id=master_id, session=session,
    )
    updated_master = await master_crud.update_obj(
        db_obj=master,
        update_data_obj=update_master_data,
        session=session,
    )
    return updated_master


@router.delete('/{master_id}', response_model=MasterDB)
async def delete_master(
    master_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    master = await master_crud.get_master_by_id(
        master_id=master_id, session=session,
    )
    deleted_master = await master_crud.delete_obj(
        obj=master, session=session,
    )
    return deleted_master
