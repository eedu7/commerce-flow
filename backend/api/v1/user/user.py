from fastapi import APIRouter

from core.dependencies.controllers import UserControllerDep

router = APIRouter()


@router.get("/")
async def get(controller: UserControllerDep):
    return await controller.get_all()


@router.post("/")
async def post(controller: UserControllerDep):
    return {"message": "Hello World"}


@router.put("/")
async def put(controller: UserControllerDep):
    return {"message": "Hello World"}


@router.delete("/")
async def delete(controller: UserControllerDep):
    return {"message": "Hello World"}
