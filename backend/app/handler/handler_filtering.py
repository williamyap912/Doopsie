from sqlalchemy.orm import Session
from app.model.models_task import Task
from app.model.enum.enum_task import PriorityEnum

def get_filtered_tasks(db: Session, completed: bool = None, priority: PriorityEnum = None, category: str = None):
    query = db.query(Task)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    if priority:
        query = query.filter(Task.priority == priority)
    if category:
        query = query.filter(Task.categories.any(category))
    return query.all()
