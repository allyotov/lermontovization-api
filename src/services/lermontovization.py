from functools import lru_cache

TEMP_RESULT_TEXT_TEMPLATE = """Говорит lermontovization-api: лермонтовизация текста сейчас находится в разработке.
Скоро мы будем присылать вам лермонтовизированный вариант вашего текста. Пока вернём его как есть: {input_text}"""

TEMP_DEMO_RESULT_TEXT_TEMPLATE = """Говорит lermontovization-api: демонстрационная лермонтовизация текста
сейчас находится в разработке. Скоро мы будем присылать вам лермонтовизированный вариант вашего текста.
Пока вернём его как есть: {input_text}"""


class LermontovizationService:
    def process_text(self, text: str) -> str:
        """Лермонтовизировать заданный текст.

        То есть вернуть текст, в котором все прилагательные заменены на "безумный" и "неземной" в той же форме, которую
        имело исходное прилагательное.
        В качестве краткой формы эпитета "неземной" будет использоваться слово "неотмирен".
        """

        # пока этот метод лишь заглушка,
        # после первичной интеграции с фронтэндом, добавим сюда полноценную лермонтовизацию текста
        return TEMP_RESULT_TEXT_TEMPLATE.format(input_text=text)

    def process_text_demo(self, text: str) -> str:
        """Метод заглушка. TODO: обновить тело метода, заменив его актуальным кодом лермонтовизации."""
        return TEMP_DEMO_RESULT_TEXT_TEMPLATE.format(input_text=text)


@lru_cache()
def get_lermontovization_service():
    return LermontovizationService()
