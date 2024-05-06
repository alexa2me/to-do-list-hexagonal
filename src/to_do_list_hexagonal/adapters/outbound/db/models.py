from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, String

from to_do_list_hexagonal.adapters.outbound.db.repositories.custom_base import (  # noqa
    Base,
)


class Task(Base):
    __tablename__ = "tasks"

    id = Column(
        String(36), primary_key=True, default=lambda: str(uuid4()), unique=True
    )
    title = Column(String(50), nullable=False)
    description = Column(String(200), nullable=True)
    status = Column(String(30))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
