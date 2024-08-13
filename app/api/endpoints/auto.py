from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import auto_crud
from app.schemas import AutoExtendDB, AutoCreate, AutoUpdate, AutoDB
from app.core.db import get_async_session

router = APIRouter()


@router.get('/', response_model=list[AutoExtendDB])
async def get_all_auto_from_db(
    session: AsyncSession = Depends(get_async_session),
):
    all_auto = await auto_crud.get_all_auto_from_db(
        session=session,
    )
    return all_auto


@router.get('/{auto_id}', response_model=AutoExtendDB)
async def get_auto_by_id(
    auto_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    auto_by_id = await auto_crud.get_auto_by_id(
        auto_id=auto_id, session=session,
    )
    return auto_by_id


@router.post('/', response_model=AutoExtendDB)
async def create_auto_from_user(
    auto_data: AutoCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_auto = await auto_crud.create_obj(
        data_obj=auto_data, session=session,
    )
    created_auto = await auto_crud.get_auto_by_id(
        auto_id=new_auto.id, session=session,
    )
    return created_auto


@router.patch('/{auto_id}', response_model=AutoExtendDB)
async def update_auto(
    auto_id: int,
    update_data: AutoUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    auto = await auto_crud.get_auto_by_id(
        auto_id=auto_id, session=session,
    )
    updated_auto = await auto_crud.update_obj(
        db_obj=auto,
        update_data_obj=update_data,
        session=session,
    )
    return updated_auto


@router.delete('/{auto_id}', response_model=AutoDB)
async def delete_auto_from_db(
    auto_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    auto_orm = await auto_crud.get_auto_by_id(
        auto_id=auto_id, session=session,
    )
    deleted_auto = await auto_crud.delete_obj(
        obj=auto_orm, session=session,
    )
    return deleted_auto
