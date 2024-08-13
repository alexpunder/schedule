__all__ = (
    'auto_router',
    'client_router',
    'work_order_router',
    'reservation_router',
    'car_post_router',
    'master_router',
    'work_router',
    'user_router',
)

from app.api.endpoints.auto import router as auto_router
from app.api.endpoints.car_post import router as car_post_router
from app.api.endpoints.client import router as client_router
from app.api.endpoints.master import router as master_router
from app.api.endpoints.reservation import router as reservation_router
from app.api.endpoints.user import router as user_router
from app.api.endpoints.work import router as work_router
from app.api.endpoints.work_order import router as work_order_router
