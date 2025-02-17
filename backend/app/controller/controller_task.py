from fastapi import Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional

from app.model.enum.enum_task import PriorityEnum, TaskTypeEnum
from app.database.database import get_db
from app.handler.handler_task import (
    create_task,
    get_tasks,
    update_task,
    delete_task,
    get_task_by_id,
)
from app.queries.schemas.schemas_task import TaskCreate``
from app.utilities.services.logger import logger

async def api_create_task(
        payload: TaskCreate,
        priority: PriorityEnum = Query(PriorityEnum.low),
        taskType: TaskTypeEnum = Query(...),
        db: Session = Depends(get_db)
        ):
    try:
        task = create_task(db,payload,priority,taskType)
        return {"message": f"Task added to {taskType.value}", "task": task}
    except SQLAlchemyError as e:
        logger.error(f"Error creating task: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
async def api_get_tasks(db: Session = Depends(get_db)):
    try:
        return {"tasks": get_tasks(db)}
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving tasks: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
async def api_get_task(
        task_id: int,
        db: Session = Depends(get_db)
        ):
    """Fetch a single task by its ID."""
    try:
        task = get_task_by_id(db, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except SQLAlchemyError as e:
        logger.error(f"Error retrieving task {task_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
async def api_update_task(
        task_id: int, 
        payload: TaskCreate,
        priority: Optional[PriorityEnum] = Query(None),
        taskType: TaskTypeEnum = Query(TaskTypeEnum.normal),
        db: Session = Depends(get_db)
        ):
    try:
        task = update_task(db,task_id,payload,priority,taskType)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task updated", "task": task}
    except SQLAlchemyError as e:
        logger.error(f"Error updating task {task_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
async def api_delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task = delete_task(db, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task deleted"}
    except SQLAlchemyError as e:
        logger.error(f"Error deleting task {task_id}: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")