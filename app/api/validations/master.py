from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Master
from app.api.validations import MODEL_OBJ_NOT_EXIST


async def check_master_exist_and_get_id(
    model: Master,
    master_id: int,
    session: AsyncSession,
) -> Master | None:
    master_obj = await session.execute(
        select(model)
        .options(
            selectinload(model.works)
        )
        .where(
            model.id == master_id
        )
    )
    master = master_obj.scalars().first()

    if not master:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=MODEL_OBJ_NOT_EXIST.get(model.__name__),
        )

    return master
