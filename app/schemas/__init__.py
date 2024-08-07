__all__ = (
    'AutoDB', 'AutoBase',
    'ClientDB',
)

from .auto import AutoDB, AutoBase
from .client import ClientDB


ClientDB.model_rebuild()
AutoDB.model_rebuild()
