from typing import Generic, Type, TypeVar

from app.models import DBBase
from core.repository import BaseRepository

ModelType = TypeVar("ModelType", bound=DBBase)


class BaseController(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], repository: BaseRepository) -> None:
        self.model = model
        self.repository = repository
