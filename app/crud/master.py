from app.crud.base import CRUDBase
from app.models import Master


class CRUDMaster(CRUDBase):
    pass


crud_master = CRUDMaster(Master)
