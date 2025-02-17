from fastapi import APIRouter
from app.controller import controller_filtering
from app.queries.schemas.schemas_task import TaskResponse

router = APIRouter()

# filtering task (GET /tasks/)
router.add_api_route(
    "/tasks/",
    controller_filtering.filter_tasks,
    methods=["GET"],
    response_model=list[TaskResponse],
)
