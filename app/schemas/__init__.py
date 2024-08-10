__all__ = (
    'AutoDB',
    'ClientDB', 'ClientFromWorkOrder',
    'WorkOrderDB', 'WorkOrderFromReservation',
    'ReservationDB', 'ReservationFromWorkOrderDB',
    'CarPostDB', 'CarPostFromReservation',
    'MasterDB', 'MasterFromWork',
    'WorkDB', 'WorkFromMaster', 'WorkFromWorkOrder',
)

from .auto import AutoDB
from .client import ClientDB, ClientFromWorkOrder
from .work_order import WorkOrderDB, WorkOrderFromReservation
from .reservation import ReservationDB, ReservationFromWorkOrderDB
from .car_post import CarPostDB, CarPostFromReservation
from .master import MasterDB, MasterFromWork
from .work import WorkDB, WorkFromMaster, WorkFromWorkOrder

ClientDB.model_rebuild()
AutoDB.model_rebuild()
WorkOrderDB.model_rebuild()
CarPostDB.model_rebuild()
MasterDB.model_rebuild()
MasterFromWork.model_rebuild()
WorkOrderFromReservation.model_rebuild()
ReservationDB.model_rebuild()
ReservationFromWorkOrderDB.model_rebuild()
ClientFromWorkOrder.model_rebuild()
CarPostFromReservation.model_rebuild()
WorkDB.model_rebuild()
WorkFromMaster.model_rebuild()
WorkFromWorkOrder.model_rebuild()
