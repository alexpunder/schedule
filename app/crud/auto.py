from app.crud.base import CRUDBase
from app.models import Auto


class CRUDAuto(CRUDBase):
    pass


crud_auto = CRUDAuto(Auto)
