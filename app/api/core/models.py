from pydantic import BaseModel, Field, IPvAnyAddress, HttpUrl


class Headers(BaseModel):
    host: str
    connection: str
    user_agent: str = Field(alias="user-agent")
    accept: str
    accept_language: str = Field(alias="accept-language")
    referer: str
    accept_encoding: str = Field(alias="accept-encoding")
    cookie: str


class CoreResponse(BaseModel):
    query_params: dict
    headers: Headers
    origin: IPvAnyAddress
    url: HttpUrl
