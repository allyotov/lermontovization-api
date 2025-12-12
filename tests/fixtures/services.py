from unittest.mock import patch

import pytest

from src.services.lermontovization import LermontovizationService


@pytest.fixture
def lermontovization_service():
    return LermontovizationService()


@pytest.fixture
def mock_process_text():
    with patch(
        'src.services.lermontovization.LermontovizationService.process_text', return_value='МОК_Привет, мир!_МОК'
    ):
        yield


@pytest.fixture
def mock_process_text_demo():
    with patch(
        'src.services.lermontovization.LermontovizationService.process_text_demo', return_value='ДЕМО_Тест_ДЕМО'
    ):
        yield
