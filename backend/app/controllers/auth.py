from app.models import DBUser
from app.repositories import UserRepository
from core.controller.base import BaseController


class AuthController(BaseController[DBUser]):
    def __init__(self, user_repository: UserRepository) -> None:
        super().__init__(model=DBUser, repository=user_repository)
        self.user_repository = user_repository
