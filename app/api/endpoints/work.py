from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud import work_crud
from app.schemas import WorkDB, WorkCreate, WorkUpdate

router = APIRouter()


@router.get('/', response_model=list[WorkDB])
async def get_all_works(
    session: AsyncSession = Depends(get_async_session),
):
    works_orm = await work_crud.get_all_works_form_db(
        session=session
    )
    all_validated_works = await work_crud.get_all_validated_model_objs(
        orm_obj=works_orm,
    )
    return all_validated_works


@router.get('/{work_id}', response_model=WorkDB)
async def get_work_by_id(
    work_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    work = await work_crud.get_work_by_id(
        work_id=work_id, session=session,
    )
    return work


@router.post('/', response_model=WorkDB)
async def create_work(
    work_data: WorkCreate,
    session: AsyncSession = Depends(get_async_session),
):
    new_work = await work_crud.create_obj(
        data_obj=work_data, session=session,
    )
    created_work = await work_crud.get_work_by_id(
        work_id=new_work.id, session=session,
    )
    return created_work


@router.patch('/{work_id}', response_model=WorkDB)
async def update_work(
    work_id: int,
    update_work_data: WorkUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    work = await work_crud.get_work_by_id(
        work_id=work_id, session=session,
    )
    updated_work = await work_crud.update_obj(
        db_obj=work,
        update_data_obj=update_work_data,
        session=session,
    )
    return updated_work


@router.delete('/{work_id}', response_model=WorkDB)
async def delete_work(
    work_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    work = await work_crud.get_work_by_id(
        work_id=work_id, session=session,
    )
    deleted_work = await work_crud.delete_obj(
        obj=work, session=session,
    )
    return deleted_work
