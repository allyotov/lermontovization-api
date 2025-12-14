import pytest


async def test_process_text(lermontovization_service, mock_repo_add_text_transformation):
    input_text = 'Привет, мир!'
    result = await lermontovization_service.process_text(input_text)

    assert isinstance(result, str)
    assert len(result) > 0


async def test_process_text_empty_string(lermontovization_service, mock_repo_add_text_transformation):
    result = await lermontovization_service.process_text('')
    assert result == ''


async def test_process_text_none(lermontovization_service, mock_repo_add_text_transformation):
    with pytest.raises(TypeError):
        await lermontovization_service.process_text(None)


# TODO: дописать тесты методов сервиса, используемых в эндпойнтах;
# TODO: написать тесты лермонтовизации как таковой - тесты корректности замены прилагательных;
