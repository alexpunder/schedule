from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Auto
from app.api.validations import MODEL_OBJ_NOT_EXIST


async def check_auto_exist_and_get_id(
    model: Auto,
    auto_id: int,
    session: AsyncSession,
) -> Auto | None:
    auto_obj = await session.execute(
        select(Auto)
        .where(
            Auto.id == auto_id
        )
        .options(
            selectinload(
                Auto.client
            )
        )
    )
    auto = auto_obj.scalars().first()

    if not auto:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=MODEL_OBJ_NOT_EXIST.get(model.__name__),
        )

    return auto
