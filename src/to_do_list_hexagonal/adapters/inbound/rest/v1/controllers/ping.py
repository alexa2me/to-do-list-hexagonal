from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/",
    status_code=200,
    tags=["Ping"],
)
def ping():
    return {"ping": "pong"}
