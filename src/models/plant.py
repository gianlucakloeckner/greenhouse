import uuid
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, constr


class TimeSeries(BaseModel):
    time: Optional[datetime] = datetime.now()
    temperature: Optional[List[float]] = []
    humidity: Optional[List[float]] = []
    light: Optional[List[float]] = []
    moisture: Optional[List[float]] = []


class Plant(BaseModel):
    id: Optional[str] = str(uuid.uuid4())
    name: str = constr(
        strip_whitespace=True, min_length=1, max_length=100)
    genetics: Optional[str] = None
    seed_planted_at: Optional[datetime] = None
    data: Optional[List[TimeSeries]] = None
    greenhouse_id: str

    def __str__(self):
        return str(self.name)

    def get_schema(self):
        print(self.schema_json(indent=2))
        return True
