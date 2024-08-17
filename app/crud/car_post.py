from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud import BaseCRUD
from app.models import CarPost
from app.schemas import CarPostDB
from app.api.validations.car_post import check_car_post_exist_and_get_id


class CarPostCRUD(BaseCRUD):

    async def get_car_post_by_id(
        self,
        car_post_id: int,
        session: AsyncSession,
    ):
        return await check_car_post_exist_and_get_id(
            model=self.model,
            car_post_id=car_post_id,
            session=session,
        )

    async def get_all_car_posts_from_db(
        self,
        session: AsyncSession,
    ):
        car_posts = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.reservation)
            )
        )
        return car_posts.scalars().all()


car_post_crud = CarPostCRUD(CarPost, CarPostDB)
