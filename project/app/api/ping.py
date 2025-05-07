from fastapi import APIRouter, Depends

from app.config import Settings, get_settings

router = APIRouter()


@router.get(
    "/ping",
    summary="Ping Server",
    responses={
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {
                        "ping": "pong!",
                        "environment": "dev",
                        "testing": False,
                    }
                }
            },
        }
    },
)
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
