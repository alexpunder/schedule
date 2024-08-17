from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CarPost
from app.api.validations import MODEL_OBJ_NOT_EXIST


async def check_car_post_exist_and_get_id(
    model: CarPost,
    car_post_id: int,
    session: AsyncSession,
) -> CarPost | None:
    car_post_obj = await session.execute(
        select(model)
        .where(
            model.id == car_post_id
        )
        .options(
            selectinload(
                model.reservation
            )
        )
    )
    car_post = car_post_obj.scalars().first()

    if not car_post:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=MODEL_OBJ_NOT_EXIST.get(model.__name__),
        )

    return car_post
