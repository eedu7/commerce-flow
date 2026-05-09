from app.models import DBUser
from app.repositories import UserRepository
from app.schemas.requests.auth import AuthIn
from app.schemas.responses.auth import AuthOut
from app.schemas.responses.user import UserOut
from core.controller.base import BaseController


class AuthController(BaseController[DBUser]):
    def __init__(self, user_repository: UserRepository) -> None:
        super().__init__(model=DBUser, repository=user_repository)
        self.user_repository = user_repository

    async def register(self, data: AuthIn) -> AuthOut:
        user = await self.create(data.model_dump())

        return AuthOut(user=UserOut.model_validate(user))
