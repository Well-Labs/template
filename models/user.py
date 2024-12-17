from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    corp_id: str
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    created_at: datetime
    updated_at: datetime