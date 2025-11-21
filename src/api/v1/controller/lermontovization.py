import logging

from fastapi import APIRouter, Request
from fastapi import status as http_status

logger = logging.getLogger("TextLermontovizationController")
lermontov_router = APIRouter(prefix="/text", tags=["text"])


@lermontov_router.post(
    "/lermontovizate",
    summary="Заказать лермонтовизацию текста",
    description="Заказать лермонтовизацию текста",
    status_code=http_status.HTTP_201_CREATED,
)
async def lermontovizate_text(request: Request):
    return {"answer": "lermontovization is under construction yet."}
