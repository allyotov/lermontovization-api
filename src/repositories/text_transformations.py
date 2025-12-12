from uuid import UUID

from databases import Database


class TextTransformationsRepository:
    def __init__(self, *, db: Database | None = None) -> None:
        super().__init__()
        self.db = db

    async def add_text_transformation(self, original_text: str, transformed_text: str, user_id: UUID | None):
        query = """
        INSERT INTO texts(original_text, transformed_text, user_id)
        VALUES (:original_text, :transformed_text, :user_id)
        """
        values = {
            'original_text': original_text,
            'transformed_text': transformed_text,
            'user_id': user_id,
        }
        async with self.db.connection() as connection:
            await connection.execute(query=query, values=values)

    async def get_text_transformations(self, user_id: UUID | None):
        query = 'SELECT * FROM texts WHERE user_id = :user_id'
        values = {'user_id': user_id}
        async with self.db.connection() as connection:
            raws = await connection.fetch_all(query=query, values=values)
        return raws  # TODO: возвращать список dataclass'ов
