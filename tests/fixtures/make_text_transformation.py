from uuid import UUID

import pytest

from src.models.text_transformation import NewTextTransformation


@pytest.fixture
def make_new_text_transformation():
    def inner(
        original_text: str,
        transformed_text: str,
        user_id: UUID | None,
        active: bool = True,
    ) -> NewTextTransformation:
        return NewTextTransformation(
            original_text=original_text,
            transformed_text=transformed_text,
            user_id=user_id,
            active=active,
        )

    return inner


@pytest.fixture
def make_text_db_record(db, make_new_text_transformation):
    async def inner(create=True, **kwargs) -> UUID:
        new_text_transformation = make_new_text_transformation(**kwargs)
        if not create:
            return new_text_transformation

        # TODO: записать компактнее, используя представление атрибутов dataclass'а как словаря:
        values = {
            'original_text': new_text_transformation.original_text,
            'transformed_text': new_text_transformation.transformed_text,
            'user_id': new_text_transformation.user_id,
            'active': new_text_transformation.active,
        }

        return await db.execute(
            query="""
            INSERT INTO texts (original_text, transformed_text, user_id, active)
            VALUES (:original_text, :transformed_text, :user_id, :active)
            RETURNING id
            """,
            values=values,
        )

    return inner
