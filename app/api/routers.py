from fastapi import APIRouter

from app.api.endpoints import (
    car_post_router, work_order_router, reservation_router, work_router,
    user_router, auto_router, client_router, master_router
)

main_router = APIRouter()

main_router.include_router(
    work_router,
    prefix='/works',
    tags=['work']
)

main_router.include_router(
    work_order_router,
    prefix='/work-orders',
    tags=['work_orders']
)

main_router.include_router(
    reservation_router,
    prefix='/reservations',
    tags=['reservation']
)

main_router.include_router(
    car_post_router,
    prefix='/car-posts',
    tags=['car_post']
)

main_router.include_router(
    master_router,
    prefix='/master',
    tags=['master']
)

main_router.include_router(
    client_router,
    prefix='/client',
    tags=['client']
)

main_router.include_router(
    auto_router,
    prefix='/auto',
    tags=['auto']
)

main_router.include_router(
    user_router,
    tags=['user']
)
