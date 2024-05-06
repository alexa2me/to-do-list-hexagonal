from sqlalchemy.orm import Session

from to_do_list_hexagonal.adapters.outbound.db.repositories.task import (
    TaskRepository,
)
from to_do_list_hexagonal.domain.entities.task import TaskModel
from to_do_list_hexagonal.domain.ports.inbound.task.dtos import CreateTaskDto


class CreateTaskUseCase:
    def __init__(self, db_session: Session):
        self.task_repository = TaskRepository(db_session)

    def create(self, task_data: CreateTaskDto):
        task_model = TaskModel(
            title=task_data.title,
            description=task_data.description,
            status=task_data.status,
        )
        return self.task_repository.create(task_model)
