__all__ = (
    'client_crud',
    'work_order_crud',
    'reservation_crud',
    'car_post_crud',
    'master_crud',
    'work_crud',
)

from .client import client_crud
from .work_order import work_order_crud
from .reservation import reservation_crud
from .car_post import car_post_crud
from .master import master_crud
from .work import work_crud
