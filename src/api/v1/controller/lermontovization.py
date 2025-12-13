import logging

from fastapi import APIRouter, Depends, Request
from fastapi import status as http_status

from src.deps import get_lermontovization_service
from src.schemes.texts import InputText, OutputText
from src.services.lermontovization import LermontovizationService

logger = logging.getLogger('TextLermontovizationController')
lermontov_router = APIRouter(prefix='/text', tags=['text'])


@lermontov_router.post(
    '/lermontovizate',
    summary='Заказать лермонтовизацию текста',
    description='Заказать лермонтовизацию текста',
    status_code=http_status.HTTP_201_CREATED,
)
async def lermontovizate_text(
    request: Request,
    input_text: InputText,
    lermontov_service: LermontovizationService = Depends(get_lermontovization_service),
) -> OutputText:
    # TODO: добавить получение user_id из jwt токена (когда будет готова авторизация):
    processed_text = await lermontov_service.process_text(text=input_text.text, user_id=None)
    return OutputText(text=processed_text)


@lermontov_router.post(
    '/demo-lermontovizate',
    summary='Заказать лермонтовизацию текста',
    description='Заказать лермонтовизацию текста',
    status_code=http_status.HTTP_201_CREATED,
)
async def demo_lermontovizate_text(
    request: Request,
    input_text: InputText,
    lermontov_service: LermontovizationService = Depends(get_lermontovization_service),
) -> OutputText:
    processed_text = await lermontov_service.process_text(text=input_text.text, user_id=None)
    return OutputText(text=processed_text)
