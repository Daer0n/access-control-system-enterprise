from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

from services.userService import UserService
from services.fileObjectService import FileObjectService
from database.database import engine
from schemas.schemas import UserCreate, UserRead
from auth.base_config import auth_backend, fastapi_users
from routers.fileObjectRouter import create_router as create_file_object_router
from routers.userRouter import create_router as create_user_router



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

async def get_user_service():
    async with SessionLocal() as session:
        async with session.begin():
            service = UserService(session)
            yield service

async def get_file_object_service():
    async with SessionLocal() as session:
        async with session.begin():
            service = FileObjectService(session)
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

user_router = create_user_router(get_user_service)
app.include_router(user_router, prefix="/user", tags=["user"])

file_router = create_file_object_router(get_file_object_service)
app.include_router(file_router, prefix="/file", tags=["file"])