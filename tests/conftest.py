import pytest

from src.services.lermontovization import LermontovizationService


@pytest.fixture
def lermontovization_service():
    return LermontovizationService()
