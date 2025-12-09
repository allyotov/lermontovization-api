from typing import Generator
from unittest.mock import patch

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.main import app as original_app
from src.services.lermontovization import LermontovizationService


@pytest.fixture
def anyio_backend():
    return 'asyncio'


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


@pytest.fixture
def app() -> FastAPI:
    return original_app


@pytest.fixture
def client(app: FastAPI) -> Generator:
    with TestClient(app=app) as client:
        yield client
