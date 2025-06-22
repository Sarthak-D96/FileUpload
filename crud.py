from fastapi import HTTPException
from sqlmodel import Session, select
from FileUpload.Database import engine
from FileUpload.auth import pwd_context
from FileUpload.models import User
from FileUpload.schemas import UserCreate, UserLogin


# user cruds
def create_user(user : UserCreate):
    user.password = pwd_context.hash(user.password)
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)


def authenticate_user(user: UserLogin):
    with Session(engine) as session:
        try:
            cry_user = session.exec(select(User).where(User.username == user.username)).first()
            if cry_user and pwd_context.verify(user.password, cry_user.password):
                return cry_user
            else:
                raise HTTPException(status_code=401, detail="Wrong username or password")
        except:
            raise HTTPException(status_code=401, detail="Wrong username or password")
