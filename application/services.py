from datetime import datetime
from domain.models import TodoItem
from typing import List, Optional
from domain.repositories import TodoRepository

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def create_todo(self, title: str, description: Optional[str] = None) -> TodoItem:
        todo = TodoItem.create(title, description)
        self.repository.add(todo)
        return todo

    def update_todo(self, todo_id: str, title: str, description: Optional[str], completed: bool) -> Optional[TodoItem]:
        todo = self.repository.get(todo_id)
        if todo:
            todo.title = title
            todo.description = description
            todo.completed = completed
            todo.updated_at = datetime.utcnow()
            self.repository.update(todo)
            return todo
        return None

    def delete_todo(self, todo_id: str) -> bool:
        todo = self.repository.get(todo_id)
        if todo:
            self.repository.delete(todo_id)
            return True
        return False

    def get_todo(self, todo_id: str) -> Optional[TodoItem]:
        return self.repository.get(todo_id)

    def list_todos(self) -> List[TodoItem]:
        return self.repository.list()
