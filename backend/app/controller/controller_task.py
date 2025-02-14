from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.handler.handler_task import create_task, get_tasks, update_task, delete_task


def api_create_task(title: str, description: str = None, db: Session = Depends(get_db)):
    task = create_task(db, title, description)
    return {"message": "Task added", "task": task}

def api_get_tasks(db: Session = Depends(get_db)):
    return {"tasks": get_tasks(db)}

def api_update_task(task_id: int, title: str, description: str, completed: bool, db: Session = Depends(get_db)):
    task = update_task(db, task_id, title, description, completed)
    if task:
        return {"message": "Task updated", "task": task}
    return {"error": "Task not found"}

def api_delete_task(task_id: int, db: Session = Depends(get_db)):
    task = delete_task(db, task_id)
    if task:
        return {"message": "Task deleted"}
    return {"error": "Task not found"}