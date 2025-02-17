from sqlalchemy import Column, Integer, String, Boolean, Enum, Date
from sqlalchemy.dialects.postgresql import ARRAY
from app.database.database import Base
from app.model.enum.enum_task import PriorityEnum, TaskTypeEnum

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False, index=True)
    priority = Column(Enum(PriorityEnum), index=True)
    start_date = Column(Date, nullable=True)
    due_date = Column(Date, nullable=True)
    categories = Column(ARRAY(String), nullable=True, default=[])
    task_type = Column(Enum(TaskTypeEnum), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'categories' in kwargs:
            self.categories = kwargs['categories']
        self.categories.append('project_name')