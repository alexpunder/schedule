from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.master import crud_master


async def check_master_exist_and_get_it(
    master_id: int,
    session: AsyncSession
):
    master = await crud_master.get(
        master_id, session
    )

    if not master:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такого мастера не существует.'
        )

    return master
