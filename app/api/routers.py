from fastapi import APIRouter

from app.api import (car_post_router, client_router, master_router,
                     reservation_router, user_router, work_order_router,
                     work_router, auto_router)

main_router = APIRouter()

main_router.include_router(
    router=work_router,
    prefix='/work',
    tags=['work']
)

main_router.include_router(
    router=work_order_router,
    prefix='/work_order',
    tags=['work_order']
)

main_router.include_router(
    router=master_router,
    prefix='/master',
    tags=['master']
)

main_router.include_router(
    router=client_router,
    prefix='/client',
    tags=['client'],
)

main_router.include_router(
    router=reservation_router,
    prefix='/reservation',
    tags=['reservation']
)

main_router.include_router(
    router=auto_router,
    prefix='/auto',
    tags=['auto']
)

main_router.include_router(
    router=user_router
)

main_router.include_router(
    router=car_post_router,
    prefix='/car_post',
    tags=['car_post']
)
