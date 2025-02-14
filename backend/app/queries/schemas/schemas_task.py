from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Schema for creating a new task (doesn't need an ID)
class TaskCreate(TaskBase):
    pass

# Schema for API responses (includes an ID)
class TaskResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True  # Allows compatibility with SQLAlchemy models