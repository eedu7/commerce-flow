from uuid import UUID

from pydantic import BaseModel, EmailStr, ConfigDict


class UserOut(BaseModel):
    uid: UUID
    email: EmailStr
    username: str

    model_config = ConfigDict(from_attributes=True)
