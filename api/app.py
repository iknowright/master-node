from fastapi import APIRouter, Depends, FastAPI
from fastapi.requests import Request
from fastapi.responses import Response
from loguru import logger

from endpoints import RESOURCES
from endpoints.wrist import model

from config import Config
from database import ENGINE

APP = FastAPI(
    version=Config.VERSION,
    title=Config.APP_TITLE,
    description=Config.APP_DESCRIPTION,
    docs_url=Config.SWAGGER_URL,
    redoc_url=Config.REDOC_URL
)
API_ROUTER = APIRouter()
model.BASE.metadata.create_all(bind=ENGINE)


# Logs incoming request information
async def log_request(request: Request):
    logger.info(f'[{request.client.host}:{request.client.host}] {request.method} {request.url}')
    logger.info(f'header: {request.headers}, body: ')
    logger.info(await request.body())


# Log response status code and body
@APP.middleware("http")
async def log_response(request: Request, call_next):
    response = await call_next(request)
    body = b""
    async for chunk in response.body_iterator:
        body += chunk

    logger.info(f'{response.status_code} {body}')

    return Response(
        content=body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )


# Add routes from resources
for resource in RESOURCES:
    API_ROUTER.add_api_route(
        resource.route,
        resource.endpoint,
        description=resource.description,
        summary=resource.summary,
        methods=[resource.method],
        responses=resource.doc,
    )

APP.include_router(API_ROUTER, dependencies=[Depends(log_request)])
