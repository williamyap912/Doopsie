from fastapi import APIRouter
from app.controller import controller_task

router = APIRouter()

# Create a new task (POST /tasks/)
router.add_api_route(
    "/tasks/create",
    controller_task.api_create_task,
    methods=["POST"],
)

# Get all tasks (GET /tasks/)
router.add_api_route(
    "/tasks/all",
    controller_task.api_get_tasks,
    methods=["GET"],
)

# Get a specific task by ID (GET /tasks/{task_id})
router.add_api_route(
    "/tasks/{task_id}",
    controller_task.api_get_task,
    methods=["GET"],
)

# Update a specific task (PATCH /tasks/{task_id})
router.add_api_route(
    "/tasks/{task_id}",
    controller_task.api_update_task,
    methods=["PATCH"],
)

# Delete a specific task (DELETE /tasks/{task_id})
router.add_api_route(
    "/tasks/{task_id}",
    controller_task.api_delete_task,
    methods=["DELETE"],
)
