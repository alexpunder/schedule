from http import HTTPStatus

from fastapi.exceptions import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Client
from app.api.validations import MODEL_OBJ_NOT_EXIST


async def check_client_exist_and_get_id(
    model: Client,
    client_id: int,
    session: AsyncSession,
) -> Client | None:
    client_obj = await session.execute(
        select(model).where(
            model.id == client_id
        )
        .options(selectinload(model.auto))
        .options(selectinload(Client.work_order))
    )
    client = client_obj.scalars().first()

    if not client:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=MODEL_OBJ_NOT_EXIST.get(model.__name__),
        )

    return client
