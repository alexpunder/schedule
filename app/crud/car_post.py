from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud import BaseCRUD
from app.models import CarPost
from app.schemas import CarPostDB


class CarPostCRUD(BaseCRUD):

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

    async def get_car_post_by_id(
        self,
        car_post_id: int,
        session: AsyncSession,
    ):
        car_post = await session.execute(
            select(self.model)
            .where(
                self.model.id == car_post_id
            )
            .options(
                selectinload(
                    self.model.reservation
                )
            )
        )
        return car_post.scalars().first()


car_post_crud = CarPostCRUD(CarPost, CarPostDB)
