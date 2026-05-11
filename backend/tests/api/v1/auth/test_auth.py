import pytest
from httpx import AsyncClient

from tests.factory.user import create_fake_user


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):

    fake_user = create_fake_user()

    response = await client.post(
        "/api/v1/auth/register",
        json=fake_user,
    )
    assert response.status_code == 201
