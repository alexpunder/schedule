from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import main_router
from app.core.admin import admin
from app.core.config import settings
from app.core.init_admin import create_superuser


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield await create_superuser()


app = FastAPI(
    title=settings.app_title,
    description=settings.description,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    router=main_router,
)

admin.mount_to(app)
