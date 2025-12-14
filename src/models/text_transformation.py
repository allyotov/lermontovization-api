from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class NewTextTransformation:
    original_text: str
    transformed_text: str
    user_id: Optional[str] = None


@dataclass
class TextTransformation:
    id: UUID
    number: int
    original_text: str
    transformed_text: str
    created_at: datetime
    user_id: Optional[str] = None
