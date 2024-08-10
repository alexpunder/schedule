__all__ = (
    'AutoDB',
    'ClientDB',
    'WorkOrderDB',
    'ReservationDB',
    'ClientFromWorkOrder',
    'ReservationFromWorkOrderDB',
    'WorkOrderFromReservation',
)

from .auto import AutoDB
from .client import ClientDB, ClientFromWorkOrder
from .work_order import WorkOrderDB, WorkOrderFromReservation
from .reservation import ReservationDB, ReservationFromWorkOrderDB

ClientDB.model_rebuild()
AutoDB.model_rebuild()
WorkOrderDB.model_rebuild()
WorkOrderFromReservation.model_rebuild()
ReservationDB.model_rebuild()
ReservationFromWorkOrderDB.model_rebuild()
ClientFromWorkOrder.model_rebuild()
