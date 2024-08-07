from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from .auto import AutoDB


class ClientBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str


class ClientDB(ClientBase):
    id: int
    auto: list['AutoDB']
