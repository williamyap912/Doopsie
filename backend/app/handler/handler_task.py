from sqlalchemy.orm import Session
from app.model.models import Task

def create_task(db: Session, title: str, description: str = None):
    new_task = Task(title=title, description=description, completed=False)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session):
    return db.query(Task).all()

def update_task(db: Session, task_id: int, title: str, description: str, completed: bool):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.title = title
        task.description = description
        task.completed = completed
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task