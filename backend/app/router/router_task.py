from fastapi import APIRouter

from app.controller import controller_task

router = APIRouter()

router.add_api_route(
    "/task/",
    controller_task.api_create_task,
    methods=["POST"],
)

router.add_api_route(
    "/task/",
    controller_task.api_get_tasks,
    methods=["GET"],
)

router.add_api_route(
    "/tasks/{task_id}",
    controller_task.api_update_task,
    methods=["PUT"],
)

router.add_api_route(
    "/tasks/{task_id}",
    controller_task.api_delete_task,
    methods=["DELETE"],
)