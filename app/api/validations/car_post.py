from typing import Optional
from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.car_post import crud_car_post
from app.schemas.car_post import CarPostDB
from app.models.car_post import CarPost


async def check_car_post_exist_and_get_it(
    car_post_id: int,
    session: AsyncSession
) -> Optional[CarPostDB]:
    car_post = await crud_car_post.get(
        car_post_id, session
    )

    if not car_post:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такого поста не существует.'
        )

    return car_post


async def check_post_name_duplicate(
    name: str,
    session: AsyncSession
) -> None:
    post = await session.execute(
        select(CarPost).where(
            CarPost.name == name
        )
    )

    if post.scalars().first():
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Пост с таким названием уже существует.'
        )
