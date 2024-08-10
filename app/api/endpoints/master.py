from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import master_crud
from app.schemas import MasterDB

router = APIRouter()


@router.get('/', response_model=list[MasterDB])
async def get_all_masters(
    session: AsyncSession = Depends(get_async_session),
):
    masters = await master_crud.get_all_masters_form_db(
        session=session
    )
    return masters
