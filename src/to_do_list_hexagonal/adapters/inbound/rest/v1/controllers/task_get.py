from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from to_do_list_hexagonal.adapters.outbound.db.database import get_session
from to_do_list_hexagonal.domain.use_cases.tasks.get_all import (
    GetAllTasksUseCase,
)

router = APIRouter()


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
