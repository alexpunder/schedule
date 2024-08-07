from pydantic import BaseModel


class AutoBase(BaseModel):
    vin_code: str
    mark: str
    model: str
    year: int
    mileage: int


class AutoDB(AutoBase):
    id: int
