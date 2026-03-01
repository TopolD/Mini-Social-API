from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, ConfigDict, model_validator


class SUserAuth(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)
