from fastapi import APIRouter, Request
from app.api.core.models import CoreResponse

router = APIRouter()


@router.get("/get")
async def get(request: Request) -> CoreResponse:
    return {
        "query_params": dict(request.query_params),
        "headers": dict(request.headers),
        "origin": request.client.host,
        "url": str(request.url),
    }
