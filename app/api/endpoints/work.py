from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import work_crud
from app.schemas import WorkDB

router = APIRouter()


@router.get('/', response_model=list[WorkDB])
async def get_all_works(
    session: AsyncSession = Depends(get_async_session),
):
    works = await work_crud.get_all_works_form_db(
        session=session
    )
    return works
