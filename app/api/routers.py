from fastapi import APIRouter

from app.api import (
    client_router, work_order_router, reservation_router,
    car_post_router,
)

main_router = APIRouter()

main_router.include_router(
    router=car_post_router,
    prefix='/car_post',
    tags=['car_post']
)

main_router.include_router(
    router=reservation_router,
    prefix='/reservation',
    tags=['reservation']
)

main_router.include_router(
    router=work_order_router,
    prefix='/work_order',
    tags=['work_order']
)

main_router.include_router(
    router=client_router,
    prefix='/client',
    tags=['client'],
)
