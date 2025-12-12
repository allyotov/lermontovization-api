import os

import pytest
from databases import Database

from src.repositories.text_transformations import TextTransformationsRepository

pytestmark = pytest.mark.anyio


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


@pytest.fixture
async def db(anyio_backend):
    database = Database(url=os.environ['TEST_DB_URL'], force_rollback=True)
    await database.connect()
    yield database
    await database.disconnect()


@pytest.fixture
async def text_transformations_repo(db):
    return TextTransformationsRepository(db=db)
