from sqlalchemy.orm import Session

from to_do_list_hexagonal.adapters.outbound.db.repositories.task import (
    TaskRepository,
)


class GetTaskByIdUseCase:
    def __init__(self, db_session: Session):
        self.task_repository = TaskRepository(db_session)

    def get_by_id(self, task_id: str):
        return self.task_repository.get_by_id(task_id)
