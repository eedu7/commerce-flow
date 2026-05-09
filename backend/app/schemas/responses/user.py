from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserOut(BaseModel):
    uid: UUID
    email: EmailStr
    username: str
