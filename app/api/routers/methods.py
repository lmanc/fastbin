from fastapi import APIRouter, Request
from app.api.core.logger import logger

router = APIRouter()


@router.get("/get")
async def get(request: Request):
    logger.info(f"Received GET request from {request.client.host}")

    return {
        "args": dict(request.query_params),
        "headers": dict(request.headers),
        "origin": request.client.host,
        "url": str(request.url),
    }
