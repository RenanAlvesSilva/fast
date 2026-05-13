from pydantic import BaseModel
from typing import List, Optional


class Store (BaseModel):
    id : Optional[int]
    name: str
    latitude: str
    longitude: str
    

class CoordsUser(BaseModel):
    latitude: float
    longitude: float
