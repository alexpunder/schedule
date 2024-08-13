from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas import AutoDB, WorkOrderFromReservation


class ClientBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


class ClientDB(ClientBase):
    id: int
    auto: list['AutoDB']
    work_order: list['WorkOrderFromReservation']


class ClientFromAuto(ClientBase):
    id: int


class ClientFromWorkOrder(ClientBase):
    id: int
    auto: list['AutoDB']


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientCreate):
    pass
