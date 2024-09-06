from typing import List, Optional
from domain.models import TodoItem
from domain.repositories import TodoRepository
from .database import get_connection
from datetime import datetime

class MySQLTodoRepository(TodoRepository):
    def add(self, todo: TodoItem) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO todos (id, title, description, completed, created_at, updated_at) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (todo.id, todo.title, todo.description, todo.completed, todo.created_at, todo.updated_at)
            )
            conn.commit()

    def get(self, todo_id: str) -> Optional[TodoItem]:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM todos WHERE id = %s", (todo_id,))
            result = cursor.fetchone()
            if result:
                return TodoItem(**result)
        return None

    def update(self, todo: TodoItem) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE todos SET title = %s, description = %s, completed = %s, updated_at = %s WHERE id = %s",
                (todo.title, todo.description, todo.completed, datetime.utcnow(), todo.id)
            )
            conn.commit()

    def delete(self, todo_id: str) -> None:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
            conn.commit()

    def list(self) -> List[TodoItem]:
        with get_connection() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM todos")
            results = cursor.fetchall()
            return [TodoItem(**result) for result in results]
