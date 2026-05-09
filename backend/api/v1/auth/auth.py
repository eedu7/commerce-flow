from uuid import UUID

from fastapi import APIRouter

from app.schemas.requests.auth import AuthIn
from core.dependencies.controllers import AuthControllerDep

router = APIRouter()


@router.post("/register")
async def register_user(data: AuthIn, controller: AuthControllerDep):
    return await controller.register(data=data)


@router.delete("/{uid}")
async def delete_user(uid: UUID, controller: AuthControllerDep):
    return await controller.delete(uid=uid)
