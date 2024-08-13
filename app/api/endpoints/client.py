from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import client_crud
from app.schemas import ClientDB

router = APIRouter()


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


@router.get('/', response_model=list[ClientDB])
async def get_all_clients(
    session: AsyncSession = Depends(get_async_session),
):
    all_clients = await client_crud.get_all_clients(session=session)
    return all_clients
