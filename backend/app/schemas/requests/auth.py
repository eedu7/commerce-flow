from pydantic import BaseModel, EmailStr, Field


class AuthBase(BaseModel):
    username: str = Field(
        ..., description="The username of the user", examples=["john_doe"]
    )
    email: EmailStr = Field(
        ..., description="The email of the user", examples=["john.doe@example.com"]
    )


class AuthIn(AuthBase):
    password: str = Field(
        ..., description="The password of the user", examples=["StrongPassword@123"]
    )


class AuthUpdate(AuthBase):
    pass
