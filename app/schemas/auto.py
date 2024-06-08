from pydantic import BaseModel, Field


class AutoBase(BaseModel):
    vin_code: str = Field(...)
    mark: str = Field(...)
    model: str = Field(...)
    year: int = Field(...)
    mileage: int = Field(...)


class AutoDB(AutoBase):
    id: int

    class Config:
        from_attributes = True


class AutoCreate(AutoBase):
    pass


class AutoUpdate(AutoBase):
    pass
