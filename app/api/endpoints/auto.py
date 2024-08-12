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
    auto_orm = await auto_crud.get_all_auto_from_db(
        session=session,
    )
    all_validated_auto = await auto_crud.get_all_validated_auto_model(
        auto_orm,
    )
    return all_validated_auto


@router.get('/{auto_id}', response_model=AutoExtendDB)
async def get_auto_by_id(
    auto_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    auto_orm = await auto_crud.get_auto_by_id(
        auto_id=auto_id, session=session,
    )
    validated_auto = await auto_crud.get_validated_auto_model(
        auto=auto_orm,
    )
    return validated_auto


@router.post('/', response_model=AutoExtendDB)
async def create_auto_from_user(
    auto_data: AutoCreate,
    session: AsyncSession = Depends(get_async_session),
):
    created_auto_orm = await auto_crud.create_auto_from_client(
        auto_data=auto_data, session=session,
    )
    validated_auto = await auto_crud.get_validated_auto_model(
        created_auto_orm,
    )
    return validated_auto


@router.patch('/{auto_id}', response_model=AutoExtendDB)
async def update_auto(
    auto_id: int,
    update_data: AutoUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    auto_orm = await auto_crud.get_auto_by_id(
        auto_id=auto_id, session=session,
    )
    updated_auto = await auto_crud.update_obj(
        db_obj=auto_orm,
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
