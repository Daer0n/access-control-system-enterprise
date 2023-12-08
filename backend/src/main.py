from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

#from operations.router import router

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
            service = Service.from_session(session)
            yield service

auth_router = create_auth_router(get_service)
app.include_router(auth_router, tags=["auth"])