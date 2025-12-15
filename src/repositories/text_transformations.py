from uuid import UUID

from databases import Database

from src.models.text_transformation import NewTextTransformation, TextTransformation


class TextTransformationsRepository:
    def __init__(self, *, db: Database | None = None) -> None:
        self.db = db

    async def add_text_transformation(self, new_text_transformation: NewTextTransformation) -> UUID:
        if new_text_transformation.user_id is None:
            query = """
            INSERT INTO texts(original_text, transformed_text)
            VALUES (:original_text, :transformed_text)
            RETURNING id
            """
            values = {
                'original_text': new_text_transformation.original_text,
                'transformed_text': new_text_transformation.transformed_text,
            }
        else:
            query = """
            INSERT INTO texts(original_text, transformed_text, user_id)
            VALUES (:original_text, :transformed_text, :user_id)
            RETURNING id
            """
            values = {
                'original_text': new_text_transformation.original_text,
                'transformed_text': new_text_transformation.transformed_text,
                'user_id': new_text_transformation.user_id,
            }
        async with self.db.connection() as connection:
            return await connection.execute(query=query, values=values)

    async def get_user_text_transformations(self, user_id: UUID | None):
        query = 'SELECT * FROM texts WHERE user_id = :user_id'
        values = {'user_id': user_id}
        async with self.db.connection() as connection:
            rows = await connection.fetch_all(query=query, values=values)
        return [TextTransformation(**dict(row)) for row in rows]

    async def get_guest_text_transformations(self):
        # TODO: добавить пагинацию (не через LIMIT OFFSET);
        # TODO: добавить сортировку по дате и номеру трансформации (возможно, в отдельном методе);
        query = 'SELECT * FROM texts'
        async with self.db.connection() as connection:
            rows = await connection.fetch_all(query=query)
        return [TextTransformation(**dict(row)) for row in rows]

    async def soft_delete_text_transformation(self, id: UUID):
        # TODO: добавить колонку updated_at в таблицу texts и обновлять её значение
        # при мягком удалении и восстановлении записей;
        query = """
        UPDATE texts
        SET active = false
        WHERE id = :id;
        """
        values = {'id': id}
        async with self.db.connection() as connection:
            await connection.execute(query=query, values=values)

    async def reactivate_text_transformation(self, id: UUID):
        query = """
        UPDATE texts
        SET active = true
        WHERE id = :id;
        """
        values = {'id': id}
        async with self.db.connection() as connection:
            await connection.execute(query=query, values=values)
