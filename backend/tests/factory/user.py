from typing import TypedDict

from faker import Faker

fake = Faker()


class FakeUser(TypedDict):
    username: str
    password: str
    email: str


def create_fake_user() -> FakeUser:
    return {
        "username": fake.user_name(),
        "password": fake.password(length=12),
        "email": fake.email(),
    }
