from typing import Any, Dict, Generic, Sequence, Type, TypeVar
from uuid import UUID

from app.models import DBBase
from core.repository import BaseRepository

ModelType = TypeVar("ModelType", bound=DBBase)


class BaseController(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], repository: BaseRepository) -> None:
        self.model = model
        self.repository = repository

    async def get_by_uid(self, uid: UUID) -> ModelType:
        obj = await self.repository.get_by_uid(uid)

        if obj is None:
            # TODO: raise not found error
            raise
        return obj

    async def get_all(self, offset: int = 0, limit: int = 100) -> Sequence[ModelType]:
        response = await self.repository.get_all(offset=offset, limit=limit)
        return response

    async def create(self, attributes: Dict[str, Any] = {}) -> ModelType:
        db_obj = await self.repository.create(attributes=attributes)
        await self.commit()
        return db_obj

    async def delete(self, uid: UUID) -> bool:
        db_obj = await self.get_by_uid(uid)

        await self.repository.delete(db_obj)
        await self.commit()
        return True

    async def update(self, uid: UUID, attributes: Dict[str, Any] = {}) -> ModelType:
        db_obj = await self.get_by_uid(uid)

        for key, value in attributes.items():
            setattr(db_obj, key, value)
        await self.commit()
        return db_obj

    async def commit(self) -> None:
        await self.repository.session.commit()
