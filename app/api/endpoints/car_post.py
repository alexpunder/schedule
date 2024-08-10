from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas import CarPostDB
from app.crud import car_post_crud

router = APIRouter()


@router.get('/', response_model=list[CarPostDB])
async def get_all_car_posts(
    session: AsyncSession = Depends(get_async_session),
):
    car_posts = await car_post_crud.get_all_car_posts_from_db(
        session=session
    )
    return car_posts
