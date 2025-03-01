from pydantic import BaseModel, HttpUrl, IPvAnyAddress


class CoreResponse(BaseModel):
    """Core response to return the same data for each request."""

    query_params: dict[str, str]
    headers: dict[str, str]
    origin: IPvAnyAddress
    url: HttpUrl
