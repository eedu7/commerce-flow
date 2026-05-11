import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(client: AsyncClient):
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "username": "john_doe",
            "email": "john.doe@example.com",
            "password": "StrongPassword@123",
        },
    )

    assert response.status_code == 201
