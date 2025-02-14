from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.handler.handler_task import create_task, get_tasks, update_task, delete_task
from app.queries.schemas.schemas_task import TaskCreate, TaskResponse


def api_create_task(
        payload: TaskCreate, 
        db: Session = Depends(get_db)
        ):
    task = create_task(db,payload)
    return {"message": "Task added", "task": task}

def api_get_tasks(
        db: Session = Depends(get_db)
        ):
    return {"tasks": get_tasks(db)}

def api_update_task(
        payload: TaskResponse,
        db: Session = Depends(get_db)
        ):
    task = update_task(db, payload)
    if task:
        return {"message": "Task updated", "task": payload}
    return {"error": "Task not found"}

def api_delete_task(
        task_id:int,
        db: Session = Depends(get_db)
        ):
    task = delete_task(db, task_id)
    if task:
        return {"message": "Task deleted"}
    return {"error": "Task not found"}