__all__ = (
    'client_router',
    'work_order_router',
    'reservation_router',
    'car_post_router',
    'master_router',
    'work_router',
)

from app.api.endpoints.client import router as client_router
from app.api.endpoints.work_order import router as work_order_router
from app.api.endpoints.reservation import router as reservation_router
from app.api.endpoints.car_post import router as car_post_router
from app.api.endpoints.master import router as master_router
from app.api.endpoints.work import router as work_router
