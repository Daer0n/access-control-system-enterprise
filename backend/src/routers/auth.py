import os 
import jwt

from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import ORJSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated, Any, AsyncGenerator, Callable, Union
from pydantic import BaseModel  
from passlib.context import CryptContext

from models.users.moderator import Moderator
from models.users.administrator import Administrator
from models.users.defaultUser import DefaultUser
from config import SECRET_AUTH
from services.userService import UserService
from repositories.userRepository import GetUserFilter
from schemas.schemas import UserCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["AUTH_ACCESS_TOKEN_EXPIRE_MINUTES"])
ALGORITHM = os.environ["AUTH_ALGORITHM"]

class Token(BaseModel):
    access_token: str
    token_type: str

def create_router(
    get_service: Callable[[], AsyncGenerator[UserService, Any]],
) -> APIRouter:
    router = APIRouter()


    @router.post("/login/{name}/{password}/")
    async def login_user(
        name: str,
        password: str,
        service: UserService = Depends(get_service),
    ):
        user = await _authenticate_user(name, password, service)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.name}, expires_delta=access_token_expires
        )
        response = ORJSONResponse(
            {"access_token": access_token, "token_type": "bearer"}
        )
        response.set_cookie(
            key="access_token",
            value=access_token,
            expires=access_token_expires.total_seconds(),
            httponly=True,
        )
        return response
    
    @router.post("/register/{name}/{email}/{password}/")
    async def register_user(
        name: str,
        email: str,
        password: str,
        service: UserService = Depends(get_service),
    ):
        hashed_password = hash_password(password)
        dto = UserCreate(
            name=name,
            password=hashed_password,
            role="DefaultUser",
            email=email,
        )
        await service.save_default_user(dto)
        return {"message": "User has been successfully registered"}
    
    @router.post("/logout/")
    async def logout_user():
        response = ORJSONResponse({"message": "User has been logged out"})
        response.delete_cookie(key="access_token")

        return response

    async def _get_user(username: str, service: UserService) -> Union[Administrator, Moderator, DefaultUser]:
        filter = GetUserFilter(name=username)
        try:
            result = await service.read_administrator(filter)
            if result:
                return result[0]
        except:
            pass
        try:
            result = await service.read_moderator(filter)
            if result:
                return result[0]
        except:
            pass
        try:
            result = await service.read_default_user(filter)
            if result:
                return result[0]
        except:
            pass
        return False
    
    def __verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    async def _authenticate_user(username: str, password: str, service: UserService) -> Union[Administrator, Moderator, DefaultUser]:
        user = await _get_user(username, service)
        if not user:
            return False
    
        if not __verify_password(password, user.hashed_password):
            return False
        
        return user
        
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_AUTH, algorithm=ALGORITHM)
        return encoded_jwt
    
    return router

def hash_password(password: str) -> str:
    return pwd_context.hash(password)