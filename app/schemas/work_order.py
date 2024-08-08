from typing import TYPE_CHECKING
from datetime import datetime

from pydantic import BaseModel

if TYPE_CHECKING:
    from .client import ClientDB


class WorkOrderBase(BaseModel):
    dt_to_create: datetime
    description: str


class WorkOrderDB(WorkOrderBase):
    id: int
    client: 'ClientDB'
