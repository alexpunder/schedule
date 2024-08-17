from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Work
from app.api.validations import MODEL_OBJ_NOT_EXIST


async def check_work_exist_and_get_id(
    model: Work,
    work_id: int,
    session: AsyncSession,
) -> Work | None:
    work_obj = await session.execute(
        select(model)
        .options(
            selectinload(model.masters)
        )
        .options(
            selectinload(model.work_order)
        )
        .where(
            model.id == work_id
        )
    )
    work = work_obj.scalars().first()

    if not work:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=MODEL_OBJ_NOT_EXIST.get(model.__name__),
        )

    return work
