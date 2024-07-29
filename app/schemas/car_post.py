from datetime import time

from pydantic import BaseModel, Field, model_validator

from app.core.constants import (
    DEFAULT_BEGIN_TIME, DEFAULT_END_TIME
)


class CarPostBase(BaseModel):
    is_active: bool
    name: str = Field(..., max_length=255)

    class Config:
        extra = 'forbid'


class CarPostDB(CarPostBase):
    id: int
    time_to_begin: time
    time_to_end: time

    class Config:
        from_attributes = True


class CarPostCreate(CarPostBase):
    time_to_begin: time = DEFAULT_BEGIN_TIME
    time_to_end: time = DEFAULT_END_TIME

    @model_validator(mode='after')
    def check_time_begin_before_end(self):
        begin = self.time_to_begin
        end = self.time_to_end

        if all([begin, end]) and begin >= end:
            raise ValueError(
                'Время начала работы поста не должно быть позже или '
                'равно времени окончания.'
            )

        return self


class CarPostUpdate(CarPostCreate):
    pass
