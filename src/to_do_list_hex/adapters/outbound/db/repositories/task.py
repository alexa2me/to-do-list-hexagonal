from sqlalchemy.orm import Session

from to_do_list_hex.adapters.outbound.db.models import Task
from to_do_list_hex.domain.entities.task import TaskModel


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

    def get_all(self) -> list[TaskModel]:
        tasks_db = self.session.query(Task).all()
        return [self._build_db_to_task_model(task_db) for task_db in tasks_db]

    def get_by_id(self, task_id: str) -> TaskModel:
        task_db = self.session.query(Task).filter(Task.id == task_id).first()
        return self._build_db_to_task_model(task_db)

    def update(self, task_id: str, entity: TaskModel) -> TaskModel:
        task_db = self.session.query(Task).filter(Task.id == task_id).first()
        task_db.title = entity.title
        task_db.description = entity.description
        task_db.status = entity.status

        self.session.commit()

        return self._build_db_to_task_model(task_db)

    def delete(self, task_id: str) -> None:
        task_db = self.session.query(Task).filter(Task.id == task_id).first()
        self.session.delete(task_db)
        self.session.commit()
