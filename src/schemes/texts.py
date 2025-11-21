from pydantic import BaseModel


class InputText(BaseModel):
    """Схема входящего текста."""

    text: str


class OutputText(BaseModel):
    """Схема исходящего текста."""

    text: str
