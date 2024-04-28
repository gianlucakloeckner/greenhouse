import uuid
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, constr

from src.models.plant import Plant


class Greenhouse(BaseModel):
    id: Optional[str] = str(uuid.uuid4())
    name: str = constr(
        strip_whitespace=True, min_length=1, max_length=100)
    description: Optional[str] = None
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
    user_email: str

    def __str__(self):
        return str(self.name)

    def get_schema(self):
        print(self.schema_json(indent=2))
        return True
