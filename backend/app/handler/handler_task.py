from sqlalchemy.orm import Session
from app.model.models import Task
from app.queries.schemas.schemas_task import TaskCreate, TaskResponse

def create_task(
        db: Session,
        task: TaskCreate,
        ):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session):
    return db.query(Task).all()

def update_task(
        db: Session,
        payload: TaskResponse,
        ):
    task = db.query(Task).filter(Task.id == payload.id).first()
    if task:
        task.title = payload.title
        task.description = payload.description
        task.completed = payload.completed
        db.commit()
        db.refresh(task)
    return task

def delete_task(
        db: Session,
        task_id: int
        ):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task