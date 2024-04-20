from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from to_do_list_hexagonal.adapters.outbound.db.database import get_session
from to_do_list_hexagonal.domain.ports.inbound.task.dtos import CreateTaskDto
from to_do_list_hexagonal.domain.use_cases.tasks.create_task import (  # noqa
    CreateTaskUseCase,
)

router = APIRouter()


@router.post(
    "/v1/task",
    status_code=201,
    tags=["Task"],
)
def create_task(
    task_data: CreateTaskDto,
    db_session: Session = Depends(get_session),
):
    try:
        use_case = CreateTaskUseCase(db_session)
        return use_case.create(task_data=task_data)
    except Exception as e:
        return {"error": str(e)}
