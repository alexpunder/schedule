__all__ = (
    'client_router',
    'work_order_router',
    'reservation_router',
)

from app.api.endpoints.client import router as client_router
from app.api.endpoints.work_order import router as work_order_router
from app.api.endpoints.reservation import router as reservation_router
