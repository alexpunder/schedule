from pydantic import BaseModel, Field

from app.schemas.auto import AutoDB


class ClientBase(BaseModel):
    first_name: str = Field(..., max_length=255)
    last_name: str = Field(..., max_length=255)
    phone_number: str = Field(..., max_length=30)

    class Config:
        extra = 'forbid'


class ClientDB(ClientBase):
    id: int
    auto_id: int

    class Config:
        from_attributes = True


class ClientWithAuto(BaseModel):
    client: ClientDB
    auto: AutoDB


class ClientCreate(ClientBase):
    auto_id: int = Field(...)


class ClientUpdate(ClientCreate):
    pass
