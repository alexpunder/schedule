from app.crud.base import CRUDBase
from app.models import CarPost


class CRUDCarPost(CRUDBase):
    pass


crud_car_post = CRUDCarPost(CarPost)
