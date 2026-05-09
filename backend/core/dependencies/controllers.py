from fastapi import Depends
from app.controllers import UserController
from typing import Annotated
from core.factory import Factory


UserControllerDep = Annotated[UserController, Depends(Factory.get_user_controller)]
