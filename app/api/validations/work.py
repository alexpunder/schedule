from typing import Optional
from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.work import WorkDB
from app.crud.work import crud_work


async def check_work_exist_and_get_it(
    work_id: int,
    session: AsyncSession
) -> Optional[WorkDB]:
    work = await crud_work.get(
        work_id, session
    )

    if not work:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Работы с таким идентификатором не существует.'
        )

    return work
