from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import WorkOrder, Work, Client
from app.api.validations import MODEL_OBJ_NOT_EXIST


async def check_work_order_exist_and_get_id(
    model: WorkOrder,
    work_order_id: int,
    session: AsyncSession,
) -> WorkOrder | None:
    work_order_obj = await session.execute(
        select(model)
        .options(
            selectinload(model.client)
            .selectinload(Client.auto)
        )
        .options(
            selectinload(model.work)
            .selectinload(Work.masters)
        )
        .options(
            selectinload(model.reservation)
        )
        .where(
            model.id == work_order_id
        )
    )
    work_order = work_order_obj.scalars().first()

    if not work_order:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=MODEL_OBJ_NOT_EXIST.get(model.__name__),
        )

    return work_order
