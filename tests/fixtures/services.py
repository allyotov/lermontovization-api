from unittest.mock import patch

import pytest

from src.services.lermontovization import LermontovizationService


@pytest.fixture
def lermontovization_service(text_transformations_repo):
    return LermontovizationService(text_transformations_repo)


@pytest.fixture
def mock_process_text():
    with patch(
        'src.services.lermontovization.LermontovizationService.process_text', return_value='МОК_Привет, мир!_МОК'
    ) as mock:
        yield mock
