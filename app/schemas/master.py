from pydantic import BaseModel, Field


class MasterBase(BaseModel):
    first_name: str = Field(..., max_length=255)
    last_name: str = Field(..., max_length=255)


class MasterDB(MasterBase):
    id: int

    class Config:
        from_attributes = True


class MasterCreate(MasterBase):
    pass


class MasterUpdate(MasterBase):
    pass
