from sqlalchemy.orm import Session
from typing import Optional
from app.model.enum.enum_task import PriorityEnum, TaskTypeEnum
from app.model.models_task import Task
from app.queries.schemas.schemas_task import TaskCreate, TaskUpdate

def create_task(
        db: Session, 
        task: TaskCreate, 
        priority: PriorityEnum,
        task_type: TaskTypeEnum,
        project_name: Optional[str] = None
        ) -> Task:
    categories = task.categories or []
    if project_name:
        categories.insert(0, project_name)
    db_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed,
        priority=priority,
        start_date=task.start_date,
        due_date=task.due_date,
        categories=categories,
        task_type=task_type
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task_by_id(
        db: Session, 
        task_id: int
        ) -> Task | None:
    """Retrieve a specific task by ID."""
    return db.query(Task).filter_by(id=task_id).one_or_none()

def update_task(
        db: Session, 
        task_id: int, 
        payload: TaskUpdate,
        priority: Optional[PriorityEnum] = None,
        task_type: Optional[TaskTypeEnum] = None,
        project_name: Optional[str] = None
        ) -> Optional[Task]:
    """Update an existing task in the database (supports partial updates)."""
    task = db.query(Task).filter_by(id=task_id).one_or_none()
    if not task:
        return None

    update_data = payload.dict(exclude_unset=True)  # Exclude unset values (partial update)
    for key, value in update_data.items():
        setattr(task, key, value)
    if priority:
        task.priority = priority
    if task_type:
        task.task_type = task_type
    if project_name:
        categories = task.categories or []
        if project_name not in categories:
            categories.insert(0, project_name)
        task.categories = categories

    db.commit()
    db.refresh(task)
    return task

def delete_task(
    db: Session, 
    task_id: int
    ) -> Task | None:
    """Delete a task from the database."""
    task = db.query(Task).filter_by(id=task_id).one_or_none()
    if not task:
        return None

    db.delete(task)
    db.commit()
    return task