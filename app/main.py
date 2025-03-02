from fastapi import FastAPI

from app.api.routers import inspection, methods

app = FastAPI(
    title='FastBin',
    version='0.1.0',
    swagger_ui_parameters={'tryItOutEnabled': True},
    openapi_tags=[
        {
            'name': 'HTTP Methods',
            'description': 'Testing different HTTP verbs.',
        },
        {
            'name': 'Request Inspection',
            'description': 'Inspect the request data.',
        },
    ],
)


app.include_router(methods.router, tags=['HTTP Methods'])
app.include_router(inspection.router, tags=['Request Inspection'])
