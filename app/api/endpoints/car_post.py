from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import car_post_crud
from app.schemas import (
    CarPostDB, CarPostFromReservation, CarPostCreate,
    CarPostUpdate,
)

router = APIRouter()


@router.get('/', response_model=list[CarPostDB])
async def get_all_car_posts(
    session: AsyncSession = Depends(get_async_session),
):
    car_posts = await car_post_crud.get_all_car_posts_from_db(
        session=session
    )
    return car_posts


@router.get('/{car_post_id}', response_model=CarPostDB)
async def get_car_post_by_id(
    car_post_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    car_post = await car_post_crud.get_car_post_by_id(
        car_post_id=car_post_id,
        session=session,
    )
    validated_car_post = await car_post_crud.get_validated_car_post_model(
        car_post=car_post,
    )
    return validated_car_post


@router.post('/', response_model=CarPostFromReservation)
async def create_car_post(
    car_post_data: CarPostCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_car_post = await car_post_crud.create_obj(
        data_obj=car_post_data,
        session=session,
    )
    return new_car_post


@router.patch('/{car_post_id}', response_model=CarPostDB)
async def update_car_post_data(
    car_post_id: int,
    update_data: CarPostUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    car_post = await car_post_crud.get_car_post_by_id(
        car_post_id=car_post_id,
        session=session,
    )
    updated_car_post = await car_post_crud.update_obj(
        db_obj=car_post,
        update_data_obj=update_data,
        session=session,
    )
    return updated_car_post


@router.delete('/{car_post_id}', response_model=CarPostDB)
async def delete_car_post_by_id(
    car_post_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    car_post = await car_post_crud.get_obj_by_id(
        id_obj=car_post_id,
        session=session,
    )
    deleted_car_post = await car_post_crud.delete_obj(
        obj=car_post,
        session=session,
    )
    return deleted_car_post
