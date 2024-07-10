from pydantic import BaseModel, EmailStr
from datetime import datetime


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str