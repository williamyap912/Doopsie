from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.handler.handler_filtering import get_filtered_tasks
from app.model.enum.enum_task import PriorityEnum

def filter_tasks(completed: bool = None, priority: PriorityEnum = None, category: str = None, db: Session = Depends(get_db)):
    try:
        tasks = get_filtered_tasks(db, completed, priority, category)
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
