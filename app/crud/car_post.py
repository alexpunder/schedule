from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import CarPost
from app.schemas import CarPostDB


class CarPostCRUD:

    def __init__(self, model):
        self.model = model

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


car_post_crud = CarPostCRUD(CarPost)
