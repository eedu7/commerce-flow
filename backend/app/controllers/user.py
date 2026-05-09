from app.models import DBUser
from app.repositories import UserRepository
from core.controller.base import BaseController


class UserController(BaseController[DBUser]):
    def __init__(self, user_repository: UserRepository) -> None:
        super().__init__(model=DBUser, repository=user_repository)
        self.user_repository = user_repository

    async def get_by_username(self, username: str) -> DBUser:
        user = await self.user_repository.get_by_username(username=username)
        if user is None:
            # TODO: raise not found error
            raise
        return user

    async def get_by_email(self, email: str) -> DBUser:
        user = await self.user_repository.get_by_email(email=email)
        if user is None:
            # TODO: raise not found error
            raise
        return user
