from functools import lru_cache


class LermontovizationService:
    def process_text(self, text: str) -> str:
        """Лермонтовизировать заданный текст.

        То есть вернуть текст, в котором все прилагательные заменены на "безумный" и "неземной" в той же форме, которую
        имело исходное прилагательное.
        В качестве краткой формы эпитета "неземной" будет использоваться слово "неотмирен".
        """

        # пока этот метод лишь заглушка,
        # после первичной интеграции с фронтэндом, добавим сюда полноценную лермонтовизацию текста
        return text


@lru_cache()
def get_lermontovization_service():
    return LermontovizationService()
