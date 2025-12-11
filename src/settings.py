from typing import Annotated

from pydantic import BaseModel, Field
from pyhocon import ConfigFactory

db_config = ConfigFactory.parse_file('settings/db.conf')


class DatabaseSettings(BaseModel):
    url: str = db_config['config']['db_url']
    min_pool_size: Annotated[int, Field(1, ge=1)] = 1
    max_pool_size: Annotated[int, Field(1, ge=1)] = 10


DB_SETTINGS = DatabaseSettings()
