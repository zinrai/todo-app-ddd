from abc import ABC, abstractmethod
from typing import List, Optional
from .models import TodoItem

class TodoRepository(ABC):
    @abstractmethod
    def add(self, todo: TodoItem) -> None:
        pass

    @abstractmethod
    def get(self, todo_id: str) -> Optional[TodoItem]:
        pass

    @abstractmethod
    def update(self, todo: TodoItem) -> None:
        pass

    @abstractmethod
    def delete(self, todo_id: str) -> None:
        pass

    @abstractmethod
    def list(self) -> List[TodoItem]:
        pass
