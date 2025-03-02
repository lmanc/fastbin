from pydantic import BaseModel, Field, HttpUrl, IPvAnyAddress


class CommonHeaders(BaseModel):
    """Common headers for all responses."""

    host: str | None = None
    connection: str | None = None
    user_agent: str | None = Field(alias='user-agent', default=None)
    accept_language: str | None = Field(alias='accept-language', default=None)
    accept_encoding: str | None = Field(alias='accept-encoding', default=None)
    referer: str | None = None
    cookie: str | None = None


class CoreResponse(BaseModel):
    """Core response to return the same data for each request."""

    query_params: dict[str, str]
    headers: CommonHeaders
    origin: IPvAnyAddress
    url: HttpUrl
