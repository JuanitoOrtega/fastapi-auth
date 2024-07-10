from pydantic import BaseModel, EmailStr
from typing import Union
from datetime import datetime


class BaseResponse(BaseModel):
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    registered_at: Union[None, datetime] = None


class UsersResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    is_active: bool
    is_verified: bool
    registered_at: datetime
    updated_at: datetime