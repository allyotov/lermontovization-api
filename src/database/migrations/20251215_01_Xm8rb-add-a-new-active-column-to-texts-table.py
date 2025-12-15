"""
add a new active column to texts table
"""

from yoyo import step

__depends__ = {'20251213_01_cWIyN-add-autogenerate-uuid-to-id-column'}

steps = [
    step(
        'ALTER TABLE texts ADD COLUMN active BOOLEAN DEFAULT TRUE;',
        """
        ALTER TABLE texts ALTER COLUMN active DROP DEFAULT;
        ALTER TABLE texts DROP COLUMN active;
        """,
    ),
]
