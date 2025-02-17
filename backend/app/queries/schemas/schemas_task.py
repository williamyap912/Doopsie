from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date
from app.model.enum.enum_task import PriorityEnum

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Task title (1-255 chars)")
    description: Optional[str] = Field(None, max_length=500, description="Optional task description (max 500 chars)")
    completed: bool = Field(False, description="Task completion status")
    start_date: Optional[date] = Field(None, description="Task start date")
    due_date: Optional[date] = Field(None, description="Task due date")
    categories: Optional[List[str]] = Field(None, description="Task categories")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None  # Allows partial updates
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    categories: Optional[List[str]] = None

class TaskResponse(TaskBase):
    id: int = Field(..., gt=0, description="Task ID (must be a positive integer)")
    priority: PriorityEnum = Field(PriorityEnum.low, description="Task priority")
    task_type: str = Field(..., description="Task type")
    project_name: str = Field(..., description="Project name")

    class Config:
        orm_mode = True  # Enables automatic ORM conversion (SQLAlchemy compatibility)
