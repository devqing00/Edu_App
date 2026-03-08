from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, Literal
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    name: Optional [str] = None    
    role: Literal ["student", "admin"]

    

class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: UUID
    is_active: bool
    model_config = ConfigDict(from_attributes=True)