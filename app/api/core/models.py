from pydantic import BaseModel, Field, HttpUrl, IPvAnyAddress


class Headers(BaseModel):
    host: str
    connection: str
    user_agent: str = Field(alias='user-agent')
    accept: str
    accept_language: str = Field(alias='accept-language', default=None)
    referer: str | None = None
    accept_encoding: str = Field(alias='accept-encoding')
    cookie: str | None = None


class CoreResponse(BaseModel):
    query_params: dict
    headers: Headers
    origin: IPvAnyAddress
    url: HttpUrl
