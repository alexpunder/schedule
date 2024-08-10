__all__ = (
    'AutoDB',
    'ClientDB',
    'WorkOrderDB',
    'ReservationDB',
    'CarPostDB',
    'ClientFromWorkOrder',
    'ReservationFromWorkOrderDB',
    'WorkOrderFromReservation',
)

from .auto import AutoDB
from .client import ClientDB, ClientFromWorkOrder
from .work_order import WorkOrderDB, WorkOrderFromReservation
from .reservation import ReservationDB, ReservationFromWorkOrderDB
from .car_post import CarPostDB

ClientDB.model_rebuild()
AutoDB.model_rebuild()
WorkOrderDB.model_rebuild()
CarPostDB.model_rebuild()
WorkOrderFromReservation.model_rebuild()
ReservationDB.model_rebuild()
ReservationFromWorkOrderDB.model_rebuild()
ClientFromWorkOrder.model_rebuild()
