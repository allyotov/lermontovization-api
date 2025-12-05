import logging

import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.router import main_router

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def _health():
    return JSONResponse(content={}, status_code=status.HTTP_200_OK)


app = FastAPI(
    docs_url='/docs/swagger',
    redoc_url='/docs/redoc',
    openapi_url='/docs/openapi.json',
)

app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['*'],
)

app.include_router(main_router)

app.get('/health', include_in_schema=False)(_health)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000,
        log_level=logging.DEBUG,
    )
