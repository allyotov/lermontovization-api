from databases import Database

from src.settings import DatabaseSettings

database = Database(
    url=DatabaseSettings.url,
    min_size=DatabaseSettings.min_pool_size,
    max_size=DatabaseSettings.max_pool_size,
)


def get_database_client() -> Database:
    return database
