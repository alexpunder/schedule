from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import auto_crud
from app.schemas import AutoExtendDB, AutoCreate
from app.core.db import get_async_session

router = APIRouter()


@router.get('/', response_model=list[AutoExtendDB])
async def get_all_auto_from_db(
    session: AsyncSession = Depends(get_async_session),
):
    auto_orm = await auto_crud.get_all_auto_from_db(
        session=session,
    )
    auto = await auto_crud.get_all_validated_auto_model(
        auto_orm,
    )
    return auto


@router.get('/{auto_id}', response_model=AutoExtendDB)
async def get_auto_by_id(
    auto_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    auto_orm = await auto_crud.get_auto_by_id(
        auto_id=auto_id, session=session,
    )
    auto = await auto_crud.get_validated_auto_model(
        auto=auto_orm,
    )
    return auto


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
