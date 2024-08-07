from fastapi import APIRouter

from app.api import client_router

main_router = APIRouter()

main_router.include_router(
    router=client_router,
    prefix='/client',
    tags=['client'],
)
