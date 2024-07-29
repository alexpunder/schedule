__all__ = (
    'Base', 'CarPost', 'Work', 'WorkOrder', 'Reservation',
    'User', 'Auto', 'Client', 'Master'
)

from app.core.db import Base
from app.models import (
    Reservation, WorkOrder, Work, CarPost,
    User, Auto, Client, Master,
)
