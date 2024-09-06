from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

class TodoItem(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime
    updated_at: datetime

    @classmethod
    def create(cls, title: str, description: Optional[str] = None):
        now = datetime.utcnow()
        return cls(
            id=str(uuid.uuid4()),
            title=title,
            description=description,
            created_at=now,
            updated_at=now
        )
