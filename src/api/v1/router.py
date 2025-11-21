import logging

from fastapi import APIRouter

from src.api.v1.controller.lermontovization import lermontov_router

logger = logging.getLogger(__file__)


api_v1_router = APIRouter(prefix="/lermontovization-api/v1")

api_v1_router.include_router(lermontov_router)
