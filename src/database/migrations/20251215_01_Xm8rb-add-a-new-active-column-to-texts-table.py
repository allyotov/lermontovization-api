"""
add a new active column to texts table
"""

from yoyo import step

__depends__ = {'20251213_01_cWIyN-add-autogenerate-uuid-to-id-column'}

steps = [
    step(
        'ALTER TABLE your_table_name ADD COLUMN active BOOLEAN DEFAULT TRUE;',
        """
        ALTER TABLE your_table_name ALTER COLUMN active DROP DEFAULT;
        ALTER TABLE your_table_name DROP COLUMN active;
        """,
    ),
]
