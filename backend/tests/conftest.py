from collections.abc import AsyncGenerator

import pytest_asyncio
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.models import DBBase
from core.config import config


@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(str(config.TEST_DATABASE_URL))

    session_local = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
    )

    async with engine.begin() as conn:
        await conn.run_sync(DBBase.metadata.create_all)

    async with session_local() as session:
        yield session

    async with engine.begin() as conn:
        await conn.run_sync(DBBase.metadata.drop_all)
