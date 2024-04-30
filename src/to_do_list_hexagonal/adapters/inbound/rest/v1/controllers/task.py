from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from to_do_list_hexagonal.adapters.outbound.db.database import get_session
from to_do_list_hexagonal.domain.ports.inbound.task.dtos import CreateTaskDto
from to_do_list_hexagonal.domain.use_cases.tasks.create import (
    CreateTaskUseCase,
)
from to_do_list_hexagonal.domain.use_cases.tasks.delete import (
    DeleteTaskUseCase,
)
from to_do_list_hexagonal.domain.use_cases.tasks.get_all import (
    GetAllTasksUseCase,
)
from to_do_list_hexagonal.domain.use_cases.tasks.get_by_id import (
    GetTaskByIdUseCase,
)
from to_do_list_hexagonal.domain.use_cases.tasks.update import (
    UpdateTaskUseCase,
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


@router.get(
    "/v1/tasks",
    status_code=200,
    tags=["Task"],
)
def get_tasks(
    db_session: Session = Depends(get_session),
):
    try:
        use_case = GetAllTasksUseCase(db_session)
        return use_case.get_all()
    except Exception as e:
        return {"error": str(e)}


@router.get(
    "/v1/task/{task_id}",
    status_code=200,
    tags=["Task"],
)
def get_task_by_id(
    task_id: str,
    db_session: Session = Depends(get_session),
):
    try:
        use_case = GetTaskByIdUseCase(db_session)
        return use_case.get_by_id(task_id=task_id)
    except Exception as e:
        return {"error": str(e)}


@router.patch(
    "/v1/task/{task_id}",
    status_code=200,
    tags=["Task"],
)
def update_task(
    task_id: str,
    task_data: CreateTaskDto,
    db_session: Session = Depends(get_session),
):
    try:
        use_case = UpdateTaskUseCase(db_session)
        return use_case.update(task_id=task_id, task_data=task_data)
    except Exception as e:
        return {"error": str(e)}


@router.delete(
    "/v1/task/{task_id}",
    status_code=200,
    tags=["Task"],
)
def delete_task(
    task_id: str,
    db_session: Session = Depends(get_session),
):
    try:
        use_case = DeleteTaskUseCase(db_session)
        return use_case.delete(task_id=task_id)
    except Exception as e:
        return {"error": str(e)}
