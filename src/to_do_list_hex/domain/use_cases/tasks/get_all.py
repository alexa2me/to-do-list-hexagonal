from sqlalchemy.orm import Session

from to_do_list_hex.adapters.outbound.db.repositories.task import (
    TaskRepository,
)


class GetAllTasksUseCase:
    def __init__(self, db_session: Session):
        self.task_repository = TaskRepository(db_session)

    def get_all(self):
        return self.task_repository.get_all()
