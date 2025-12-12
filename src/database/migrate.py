import logging

from yoyo import get_backend, read_migrations

from src.settings import DB_SETTINGS

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    backend = get_backend(DB_SETTINGS.url)
    migrations = read_migrations('./src/database/migrations')
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))
    logger.info('Migrations were applied!')
