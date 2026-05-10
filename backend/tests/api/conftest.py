from typing import AsyncGenerator

import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

from core.server import server


@pytest_asyncio.fixture(scope="session")
async def app():
    """
    Create a new FastAPI app instance for testing.
    """
    application = server()

    async with LifespanManager(application) as manager:
        yield manager.app


@pytest_asyncio.fixture(scope="function")
async def client(app) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
