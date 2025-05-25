
from pydantic import BaseModel
from typing import Optional

class TokenData(BaseModel):
    username: str
    role: str