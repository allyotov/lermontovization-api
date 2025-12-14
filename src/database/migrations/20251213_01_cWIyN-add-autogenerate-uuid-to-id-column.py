"""
add autogenerate uuid to id column
"""

from yoyo import step

__depends__ = {'20251209_01_NYP5u-create-text-transformations-table'}

steps = [
    step(
        'ALTER TABLE texts ALTER COLUMN id SET DEFAULT gen_random_uuid();',
        'ALTER TABLE texts ALTER COLUMN id DROP DEFAULT;',
    )
]
