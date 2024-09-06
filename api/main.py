from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from application.services import TodoService
from infrastructure.repositories import MySQLTodoRepository
from domain.models import TodoItem
from infrastructure.database import initialize_database

app = FastAPI()

# Database initialization
@app.on_event("startup")
async def startup_event():
    initialize_database()

# Dependency Injection
todo_repository = MySQLTodoRepository()
todo_service = TodoService(todo_repository)

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool

@app.post("/todos", response_model=TodoItem)
def create_todo(todo: TodoCreate):
    return todo_service.create_todo(todo.title, todo.description)

@app.get("/todos/{todo_id}", response_model=TodoItem)
def get_todo(todo_id: str):
    todo = todo_service.get_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: str, todo: TodoUpdate):
    updated_todo = todo_service.update_todo(todo_id, todo.title, todo.description, todo.completed)
    if updated_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo

@app.delete("/todos/{todo_id}", response_model=bool)
def delete_todo(todo_id: str):
    deleted = todo_service.delete_todo(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return True

@app.get("/todos", response_model=List[TodoItem])
def list_todos():
    return todo_service.list_todos()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
