from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from src.main import app as original_app


@pytest.fixture
def app() -> FastAPI:
    return original_app


@pytest.fixture
def client(app: FastAPI) -> Generator:
    with TestClient(app=app) as client:
        yield client
