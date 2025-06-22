import datetime
from email.policy import default
from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel,table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    username : str
    email : str
    password : str


class UploadedFile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str
    filepath: str
    upload_time: datetime = Field(default_factory=datetime.utcnow)
    user_id: int = Field(foreign_key="user.id")

