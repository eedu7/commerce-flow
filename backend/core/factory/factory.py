from typing import Annotated

from fastapi import Depends

from app.controllers import UserController
from app.repositories import UserRepository
from core.dependencies.session import AsyncSessionDep


class Factory:
    # Repositories
    @staticmethod
    async def get_user_repository(session: AsyncSessionDep) -> UserRepository:
        return UserRepository(session=session)

    # Controllers
    @staticmethod
    async def get_user_controller(
        user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    ) -> UserController:
        return UserController(user_repository=user_repository)
