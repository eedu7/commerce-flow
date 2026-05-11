from typing import AsyncGenerator

import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

from core.database import get_async_session
from core.server import server


@pytest_asyncio.fixture(scope="function")
async def app(db_session):
    """
    Create a new FastAPI app instance for testing.
    """

    async def _get_session():
        return db_session

    application = server()
    application.dependency_overrides[get_async_session] = _get_session

    async with LifespanManager(application) as manager:
        yield manager.app


@pytest_asyncio.fixture(scope="function")
async def client(app) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
