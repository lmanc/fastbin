from fastapi import FastAPI
from app.api.routers import methods

app = FastAPI(
    title="FastBin",
    version="0.1.0",
    swagger_ui_parameters={"tryItOutEnabled": True},
)


app.include_router(methods.router)
