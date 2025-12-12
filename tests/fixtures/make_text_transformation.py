import datetime
from uuid import UUID

import pytest

from src.models.text_transformation import TextTransformation


@pytest.fixture
def make_text_transformation():
    def inner(
        id: UUID,
        number: int,
        original_text: str,
        transformed_text: str,
        created_at: datetime,
        user_id: UUID | None,
    ) -> TextTransformation:
        return TextTransformation(
            id=id,
            number=number,
            original_text=original_text,
            transformed_text=transformed_text,
            created_at=created_at,
            user_id=user_id,
        )

    return inner


@pytest.fixture
def make_text_db_record(db, make_group_text_transformation):
    async def inner(create=True, **kwargs):
        text_transformation = make_group_text_transformation(**kwargs)
        if not create:
            return text_transformation

        # TODO: записать компактнее, используя представление атрибутов dataclass'а как словаря:
        values = {
            'id': text_transformation.id,
            'number': text_transformation.number,
            'original_text': text_transformation.original_text,
            'transformed_text': text_transformation.transformed_text,
            'created_at': text_transformation.create_at,
            'user_id': text_transformation.user_id,
        }

        await db.execute(
            query="""
            INSERT INTO text (id, number, original_text, transformed_text, created_at, user_id)
            VALUES (:id, :number, :original_text, :transformed_text, :created_at, :user_id)
            """,
            values=values,
        )

    return inner
