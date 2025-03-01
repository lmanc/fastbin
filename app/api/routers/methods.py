from fastapi import APIRouter, Request

from app.api.core import CoreResponse, logger

router = APIRouter()


@router.get('/get')
async def get(request: Request) -> CoreResponse:
    logger.info(f'Received {request.method} request on {request.url} from {request.client.host}')

    return {
        'query_params': dict(request.query_params),
        'headers': dict(request.headers),
        'origin': request.client.host,
        'url': str(request.url),
    }
