from app.crud.base import CRUDBase
from app.models import Work


class CRUDWork(CRUDBase):
    pass


crud_work = CRUDWork(Work)
