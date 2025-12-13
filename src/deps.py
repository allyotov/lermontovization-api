from databases import Database
from fastapi import Depends

from src.repositories.text_transformations import TextTransformationsRepository
from src.services.lermontovization import LermontovizationService
from src.settings import DB_SETTINGS

database = Database(
    url=DB_SETTINGS.url,
    min_size=DB_SETTINGS.min_pool_size,
    max_size=DB_SETTINGS.max_pool_size,
)


def get_database_client() -> Database:
    return database


def get_texts_transformation_repo(db: Database = Depends(get_database_client)):
    return TextTransformationsRepository(db=db)


def get_lermontovization_service(
    texts_transformations_repo: TextTransformationsRepository = Depends(get_texts_transformation_repo),
):
    return LermontovizationService(texts_repo=texts_transformations_repo)
