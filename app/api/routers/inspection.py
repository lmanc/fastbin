from fastapi import APIRouter, Request

from app.api.core import HeadersResponse, logger

router = APIRouter()


@router.get('/headers', summary="Return the incoming request's HTTP headers.")
async def headers(request: Request) -> HeadersResponse:
    """Headers endpoint."""
    logger.info(f'Received {request.method} request on {request.url} from {request.client.host}')

    return {'headers': dict(request.headers)}
