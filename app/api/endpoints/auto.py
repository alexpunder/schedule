from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.auto import AutoDB, AutoCreate, AutoUpdate
from app.crud.auto import crud_auto


router = APIRouter()


@router.get(
    '/{auto_id}',
    response_model=AutoDB
)
async def get_auto(
    auto_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    auto = await crud_auto.get(
        auto_id, session
    )
    return auto


@router.get(
    '/',
    response_model=list[AutoDB]
)
async def get_all_auto(
    session: AsyncSession = Depends(get_async_session)
):
    all_auto = await crud_auto.get_all(
        session
    )
    return all_auto


@router.post(
    '/create/',
    response_model=AutoDB
)
async def create_auto(
    auto: AutoCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_auto = await crud_auto.create(
        auto, session
    )
    return new_auto


@router.patch(
    '/update/{auto_id}',
    response_model=AutoUpdate
)
async def update_auto(
    auto_id: int,
    auto_update_data: AutoUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    auto = await crud_auto.get(
        auto_id, session
    )
    updated_auto = await crud_auto.update(
        auto, auto_update_data, session
    )
    return updated_auto


@router.delete(
    '/delete/{auto_id}',
    response_model=AutoDB
)
async def delete_auto(
    auto_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    auto = await crud_auto.get(
        auto_id, session
    )
    auto = await crud_auto.delete(
        auto, session
    )
    return auto
