"""
Create texts table for storing text transformations
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
        CREATE TABLE texts (
            id UUID PRIMARY KEY,
            number BIGINT GENERATED ALWAYS AS IDENTITY,
            original_text VARCHAR(1024),
            transformed_text VARCHAR(2048),
            created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
            user_id UUID DEFAULT NULL
        );

        -- Индекс для ускорения поиска по number
        CREATE INDEX idx_texts_number ON texts(number);
        """,
        """
        DROP INDEX IF EXISTS idx_texts_number;
        DROP TABLE IF EXISTS texts;
        """,
    )
]
