from uuid import UUID

from fastapi import APIRouter

from app.schemas.requests.auth import AuthUpdate
from core.dependencies.controllers import UserControllerDep

router = APIRouter()


@router.get("/")
async def get(controller: UserControllerDep):
    return await controller.get_all()


@router.post("/")
async def post(controller: UserControllerDep):
    return {"message": "Hello World"}


@router.put("/{uid}")
async def put(uid: UUID, data: AuthUpdate, controller: UserControllerDep):
    return await controller.update(uid=uid, attributes=data.model_dump())


@router.delete("/{uid}")
async def delete(uid: UUID, controller: UserControllerDep):
    return await controller.delete(uid=uid)
