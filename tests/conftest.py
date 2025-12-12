pytest_plugins = [
    'tests.fixtures.repositories.anyio_backend',
    'tests.fixtures.repositories.db',
    'tests.fixtures.repositories.text_transformations_repo',
    'tests.fixtures.api_client.app',
    'tests.fixtures.api_client.client',
    'tests.fixtures.make_test_transformation.make_text_db_record',
    'tests.fixtures.make_test_transformation.make_text_transformation',
]
