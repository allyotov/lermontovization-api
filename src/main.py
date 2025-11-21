import logging

import uvicorn
from fastapi import FastAPI

from src.router import main_router

app = FastAPI(
    docs_url="/lermontovization-api/docs/swagger",
    redoc_url="/lermontovization-api/redoc",
    openapi_url="/lermontovization-api/openapi.json",
)

app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level=logging.DEBUG,
    )
