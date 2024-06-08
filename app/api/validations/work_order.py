from typing import Optional
from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.work_order import WorkOrderDB
from app.crud.work_order import crud_work_order


async def check_work_order_exist_and_get_it(
    work_order_id: int,
    session: AsyncSession,
    get_object=True,
    exception=True
) -> Optional[WorkOrderDB]:
    work_order = await crud_work_order.get(
        work_order_id, session
    )

    if not work_order and exception:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такого заказ-наряда не существует.'
        )

    if get_object:
        return work_order
