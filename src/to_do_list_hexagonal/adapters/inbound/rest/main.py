from fastapi import FastAPI

from to_do_list_hexagonal.adapters import settings
from to_do_list_hexagonal.adapters.inbound.rest.v1.controllers.ping import (
    router as ping_router,
)
from to_do_list_hexagonal.adapters.inbound.rest.v1.controllers.task import (
    router as task_router,
)


def get_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME)

    application.include_router(task_router)
    application.include_router(ping_router)

    return application


app = get_application()
