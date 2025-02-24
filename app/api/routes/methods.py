from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/get")
async def get(request: Request):
    return {
        "args": dict(request.query_params),
        "headers": dict(request.headers),
        "origin": request.client.host,
        "url": str(request.url),
    }
