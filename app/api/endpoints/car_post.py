from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.car_post import (
    CarPostDB, CarPostCreate, CarPostUpdate
)
from app.core.db import get_async_session
from app.crud.car_post import crud_car_post
from app.api.validations.car_post import (
    check_car_post_exist_and_get_it, check_post_name_duplicate
)


router = APIRouter()


@router.get(
    '/{post_id}',
    response_model=CarPostDB
)
async def get_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    post = await check_car_post_exist_and_get_it(
        post_id, session
    )
    return post


@router.get(
    '/',
    response_model=list[CarPostDB]
)
async def get_all_posts(
    session: AsyncSession = Depends(get_async_session)
):
    all_posts = await crud_car_post.get_all(
        session
    )
    return all_posts


@router.post(
    '/',
    response_model=CarPostDB
)
async def create_post(
    post: CarPostCreate,
    session: AsyncSession = Depends(get_async_session)
):
    await check_post_name_duplicate(
        post.name, session
    )
    new_post = await crud_car_post.create(
        post, session
    )
    return new_post


@router.patch(
    '/{post_id}',
    response_model=CarPostDB
)
async def update_post(
    post_id: int,
    update_data: CarPostUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    post = await check_car_post_exist_and_get_it(
        post_id, session
    )
    updated_post = await crud_car_post.update(
        post, update_data, session
    )
    return updated_post


@router.delete(
    '/{post_id}',
    response_model=CarPostDB
)
async def delete_post(
    post_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    post = await check_car_post_exist_and_get_it(
        post_id, session
    )
    deleted_post = await crud_car_post.delete(
        post, session
    )
    return deleted_post
