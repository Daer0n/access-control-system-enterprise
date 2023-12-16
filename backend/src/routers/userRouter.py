import os
#import jwt

from typing import Annotated, Any, AsyncGenerator, Callable, Optional
#from jose import JWTError

from fastapi import APIRouter, Depends, Form, HTTPException, Query, Request, status
from pydantic import BaseModel

from repositories.userRepository import GetUserFilter, PatchUserFilter
from services.userService import UserService
from schemas.schemas import UserCreate


SECRET_KEY = os.environ["SECRET_AUTH"]
ALGORITHM = os.environ["AUTH_ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["AUTH_ACCESS_TOKEN_EXPIRE_MINUTES"])

class TokenData(BaseModel):
    username: str | None = None

def create_router(
    get_service: Callable[[], AsyncGenerator[UserService, Any]],
) -> APIRouter:
    router = APIRouter()

    # async def get_current_user(
    #     request: Request,
    #     service: UserService = Depends(get_service),
    # ):
    #     credentials_exception = HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Could not validate credentials",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )

    #     token = request.cookies.get("access_token")
    #     if not token:
    #         raise credentials_exception

    #     try:
    #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #         username: str = payload.get("sub")
    #         if username is None:
    #             raise credentials_exception
    #         token_data = TokenData(username=username)
    #     except JWTError:
    #         raise credentials_exception
    #     result = await service.read_administator(
    #         filter=GetUserFilter(full_name=token_data.username)
    #     )
    #     assert len(result) == 1
    #     user = result[0]

    #     if user is None:
    #         raise credentials_exception
    #     return user

    @router.post(
        "/administrator/{name}/{email}/{password}/",
        name="Add administrator",
    )
    async def add_administator(
        name: str, 
        email: str, 
        password: str,
        service: UserService = Depends(get_service),
    ):
        dto = UserCreate(
            name=name,
            email=email,
            role='Administrator',
            password=password
        )
        return await service.save_administrator(dto)
    
    @router.delete(
        "/administrator/{id}/",
        name="Delete administrator",
    )
    async def delete_administrator(
        id: int,
        name: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = GetUserFilter(
            id=id,
            name=name
        )
        return await service.delete_administrator(filter)
    
    @router.get(
        "/administrator/{id}/",
        name="Get administrator",
    )
    async def read_administator(
        id: int,
        name: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = GetUserFilter(
            id=id,
            name=name
        )
        return await service.read_administator(filter)


    @router.patch(
        "/administrator/{id}/",
        name="Patch administrator",
    )
    async def update_administrator(
        id: int, 
        name: Optional[str] = None,
        email: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = PatchUserFilter(       
            id=id, 
            name=name,
            email=email,
        )
        return await service.update_administrator(filter)

    @router.get(
        "/administrator/user/{user_id}/",
        name="Change role to moderator",
    )
    async def change_user_role(
        user_id: int, 
        name: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = GetUserFilter(       
            id=user_id, 
            name=name,
        )
        return await service.change_user_role(filter)
    
    @router.get(
        "/administrator/moderator/{moderator_id}/",
        name="Change role to moderator",
    )
    async def change_user_role(
        moderator_id: int, 
        name: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = GetUserFilter(       
            id=moderator_id, 
            name=name,
        )
        return await service.change_moderator_role(filter)

    @router.post(
        "/moderator/{name}/{email}/{password}/",
        name="Add moderator",
    )
    async def add_moderator(
        name: str, 
        email: str, 
        password: str,
        service: UserService = Depends(get_service),
    ):
        dto = UserCreate(
            name=name,
            email=email,
            role='Moderator',
            password=password
        )
        return await service.save_moderator(dto)
    
    @router.delete(
        "/moderator/{id}/",
        name="Delete moderator",
    )
    async def delete_moderator(
        id: int,
        name: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = GetUserFilter(
            id=id,
            name=name
        )
        return await service.delete_moderator(filter)
    
    @router.get(
        "/moderator/{id}/",
        name="Get moderator",
    )
    async def read_moderator(
        id: int,
        name: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = GetUserFilter(
            id=id,
            name=name
        )
        return await service.read_moderator(filter)


    @router.patch(
        "/moderator/{id}/",
        name="Patch moderator",
    )
    async def update_moderator(
        id: int, 
        name: Optional[str] = None,
        email: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = PatchUserFilter(
            id=id, 
            name=name,
            email=email,
        )
        return await service.update_moderator(filter)
    
    @router.post(
        "/user/{name}/{email}/{password}/",
        name="Add default user",
    )
    async def add_default_user(
        name: str, 
        email: str, 
        password: str,
        service: UserService = Depends(get_service),
    ):
        dto = UserCreate(
            name=name,
            email=email,
            role='DefaultUser',
            password=password
        )
        return await service.save_default_user(dto)
    
    @router.delete(
        "/user/{id}/",
        name="Delete default user",
    )
    async def delete_default_user(
        id: int,
        name: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = GetUserFilter(
            id=id,
            name=name
        )
        return await service.delete_default_user(filter)
    
    @router.get(
        "/user/{id}/",
        name="Get default user",
    )
    async def read_default_user(
        id: int,
        name: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = GetUserFilter(
            id=id,
            name=name
        )
        return await service.read_default_user(filter)


    @router.patch(
        "user/{id}/",
        name="Patch default user",
    )
    async def update_default_user(
        id: int, 
        name: Optional[str] = None,
        email: Optional[str] = None,
        service: UserService = Depends(get_service),
    ):
        filter = PatchUserFilter(
            id=id, 
            name=name,
            email=email,
        )
        return await service.update_default_user(filter)
        
    

    return router
