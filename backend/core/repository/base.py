from collections.abc import Sequence
from typing import Any, Dict, Generic, Type, TypeVar
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import DBBase

ModelType = TypeVar("ModelType", bound=DBBase)


class BaseRepository(Generic[ModelType]):
    """Base class for repositories."""

    def __init__(self, model: Type[ModelType], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def create(self, attributes: Dict[str, Any] = {}) -> ModelType:
        """Create a new record."""
        instance = self.model(**attributes)
        self.session.add(instance)
        return instance

    async def get_all(
        self,
        offset: int = 0,
        limit: int = 100,
    ) -> Sequence[ModelType]:
        stmt = select(self.model).offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_uid(self, uid: UUID) -> ModelType | None:
        return await self.session.get(self.model, uid)

    async def delete(self, instance: ModelType) -> None:
        await self.session.delete(instance)

    async def get_by(self, field: str, value: Any) -> ModelType | None:

        if not getattr(self.model, field, None):
            raise ValueError(f"Model {self.model.__name__} does not have field {field}")

        stmt = select(self.model).where(getattr(self.model, field) == value)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
