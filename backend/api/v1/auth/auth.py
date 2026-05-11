from uuid import UUID

from fastapi import APIRouter, status

from app.schemas.requests.auth import AuthIn
from core.dependencies.controllers import AuthControllerDep

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(data: AuthIn, controller: AuthControllerDep):
    return await controller.register(data=data)


@router.delete("/{uid}")
async def delete_user(uid: UUID, controller: AuthControllerDep):
    return await controller.delete(uid=uid)
