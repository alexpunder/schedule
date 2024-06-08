from datetime import datetime

from pydantic import BaseModel


class WorkOrderBase(BaseModel):
    description: str


class WorkOrderDB(WorkOrderBase):
    dt_to_create: datetime
    id: int

    class Config:
        from_attributes = True


class WorkOrderCreate(WorkOrderBase):
    pass


class WorkOrderUpdate(WorkOrderBase):
    pass
