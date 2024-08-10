from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from .auto import AutoDB
    from .work_order import WorkOrderFromReservation


class ClientBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


class ClientDB(ClientBase):
    id: int
    auto: list['AutoDB']
    work_order: list['WorkOrderFromReservation']


class ClientFromWorkOrder(ClientBase):
    id: int
    auto: list['AutoDB']
