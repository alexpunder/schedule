from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from app.schemas.client import (
    ClientDB, ClientCreate, ClientWithAuto, ClientUpdate
)
from app.core.db import get_async_session
from app.crud.client import crud_client
from app.crud.auto import crud_auto


router = APIRouter()


@router.get(
    '/{client_id}',
    response_model=ClientDB
)
async def get_client(
    client_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    client = await crud_client.get(
        client_id, session
    )
    return client


@router.get(
    '/',
    response_model=list[ClientDB]
)
async def get_all_clients(
    session: AsyncSession = Depends(get_async_session)
):
    clients = await crud_client.get_all(
        session
    )
    return clients


@router.post(
    '/',
    response_model=ClientWithAuto
)
async def create_client(
    client: ClientCreate,
    session: AsyncSession = Depends(get_async_session)
):
    new_client, auto_id = await crud_client.create(
        client, session
    )
    client_auto = await crud_auto.get(
        auto_id, session
    )
    result = {'client': new_client, 'auto': client_auto}
    return result


@router.patch(
    '/{client_id}',
    response_model=ClientUpdate
)
async def update_client(
    client_id: int,
    client_updated_data: ClientUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    client = await crud_client.get(
        client_id, session
    )
    updated_client = await crud_client.update(
        client, client_updated_data, session
    )
    return updated_client


@router.delete(
    '/{client_id}',
    response_model=ClientDB
)
async def delete_client(
    client_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    client = await crud_client.get(
        client_id, session
    )
    deleted_client = await crud_client.delete(
        client, session
    )
    return deleted_client
