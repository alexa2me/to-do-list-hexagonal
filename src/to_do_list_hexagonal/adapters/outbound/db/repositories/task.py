from sqlalchemy.orm import Session

from to_do_list_hexagonal.adapters.outbound.db.models import Task
from to_do_list_hexagonal.domain.entities.task import TaskModel


class TaskRepository:
    def __init__(self, db_session: Session):
        self.session = db_session

    def __to_db_model(self, task: TaskModel) -> Task:
        return Task(
            title=task.title,
            description=task.description,
            status=task.status,
        )

    def _build_db_to_task_model(self, task_db: Task) -> TaskModel:
        return TaskModel(
            id=task_db.id,
            title=task_db.title,
            description=task_db.description,
            status=task_db.status,
            created_at=task_db.created_at,
            updated_at=task_db.updated_at,
        )

    def create(self, entity: TaskModel) -> TaskModel:
        task_db = self.__to_db_model(entity)

        self.session.add(task_db)
        self.session.commit()

        return self._build_db_to_task_model(task_db)
