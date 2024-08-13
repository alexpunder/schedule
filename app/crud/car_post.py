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
        car_posts_orm = car_posts.scalars().all()
        result = [
            CarPostDB.model_validate(row, from_attributes=True)
            for row in car_posts_orm
        ]
        return result

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

    async def get_validated_car_post_model(
        self,
        car_post: CarPost,
    ):
        return CarPostDB.model_validate(
            car_post, from_attributes=True
        )


car_post_crud = CarPostCRUD(CarPost)
