from sqlalchemy.orm import Session

from to_do_list_hexagonal.adapters.outbound.db.repositories.task import (
    TaskRepository,
)


class DeleteTaskUseCase:
    def __init__(self, db_session: Session):
        self.task_repository = TaskRepository(db_session)

    def delete(self, task_id: str):
        return self.task_repository.delete(task_id)
