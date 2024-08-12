from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas import ClientFromAuto


class AutoBase(BaseModel):
    vin_code: str
    mark: str
    model: str
    year: int
    mileage: int


class AutoDB(AutoBase):
    id: int


class AutoExtendDB(AutoBase):
    id: int
    client: 'ClientFromAuto'


class AutoCreate(AutoBase):
    client_id: int


class AutoUpdate(AutoCreate):
    pass
