from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import client_crud
from app.schemas import ClientDB, ClientCreate, ClientUpdate

router = APIRouter()


@router.get('/', response_model=list[ClientDB])
async def get_all_clients(
    session: AsyncSession = Depends(get_async_session),
):
    clients = await client_crud.get_all_clients(session=session)
    return clients


@router.get('/{client_id}', response_model=ClientDB)
async def get_client_by_id(
    client_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    client = await client_crud.get_client_by_id(
        client_id=client_id,
        session=session,
    )
    return client


@router.post('/', response_model=ClientDB)
async def create_client(
    client_data: ClientCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_client = await client_crud.create_obj(
        data_obj=client_data, session=session,
    )
    created_client = await client_crud.get_client_by_id(
        client_id=new_client.id, session=session,
    )
    return created_client


@router.patch('/{client_id}', response_model=ClientDB)
async def update_client(
    client_id: int,
    update_client_data: ClientUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    client = await client_crud.get_client_by_id(
        client_id=client_id, session=session,
    )
    updated_client = await client_crud.update_obj(
        db_obj=client,
        update_data_obj=update_client_data,
        session=session,
    )
    return updated_client


@router.delete('/{client_id}', response_model=ClientDB)
async def delete_client(
    client_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    client = await client_crud.get_client_by_id(
        client_id=client_id, session=session,
    )
    deleted_client = await client_crud.delete_obj(
        obj=client, session=session,
    )
    return deleted_client
