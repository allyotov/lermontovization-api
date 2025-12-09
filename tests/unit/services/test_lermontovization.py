import pytest


class TestLermontovizationService:
    def test_process_text_basic(self, lermontovization_service):
        input_text = 'Привет, мир!'
        result = lermontovization_service.process_text(input_text)

        assert isinstance(result, str)
        assert len(result) > 0

    def test_process_text_empty_string(self, lermontovization_service):
        result = lermontovization_service.process_text('')
        assert result == ''

    def test_process_text_none(self, lermontovization_service):
        with pytest.raises(TypeError):
            lermontovization_service.process_text(None)

    def test_process_text_demo_basic(self, lermontovization_service):
        input_text = 'Пример текста'
        result = lermontovization_service.process_text_demo(input_text)

        assert isinstance(result, str)
        assert len(result) > 0

    # TODO: дописать тесты метода демонстрационного преобразования текста;
    # TODO: написать тесты лермонтовизации как таковой - тесты корректности замены прилагательных;
