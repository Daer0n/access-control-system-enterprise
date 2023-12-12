from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker
from services.userService import UserService
from database.database import engine

from schemas.schemas import UserCreate, UserRead
from auth.base_config import auth_backend, fastapi_users
from routers.auth import create_router as create_auth_router


app = FastAPI(
    title="Access contorl system entreprise"
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PATCH"],
    allow_headers=["*"],
)

SessionLocal = async_sessionmaker(expire_on_commit=False, bind=engine)

async def get_service():
    async with SessionLocal() as session:
        async with session.begin():
            service = UserService(session)
            yield service

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
