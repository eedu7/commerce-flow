from pydantic import BaseModel, ConfigDict

from app.schemas.responses.user import UserOut


class AuthOut(BaseModel):
    user: UserOut

    model_config = ConfigDict(from_attributes=True)
