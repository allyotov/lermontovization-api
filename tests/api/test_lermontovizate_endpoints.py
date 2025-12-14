import httpx
import pytest
from fastapi import status


@pytest.mark.usefixtures('mock_process_text')
def test_lermontovizate_text_success(client: httpx.AsyncClient):
    response = client.post('/lermontovization-api/v1/text/lermontovizate', json={'text': 'Привет, мир!'})

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data['text'] == 'МОК_Привет, мир!_МОК'


@pytest.mark.usefixtures('mock_process_text')
def test_demo_lermontovizate_text_success(client: httpx.AsyncClient):
    response = client.post('/lermontovization-api/v1/text/demo-lermontovizate', json={'text': 'Тест'})

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data['text'] == 'МОК_Привет, мир!_МОК'


# TODO: добавить тесты валидации длины текста;
