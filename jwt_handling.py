
from _pydatetime import timedelta

from fastapi import HTTPException, Depends
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime
from FileUpload.auth import SECRET_KEY
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    username : str

def create_access_token(data:dict, expires_delta:timedelta or None = None):
     to_encode = data.copy()

     if expires_delta:
         expire_time = datetime.utcnow() + expires_delta
     else:
         expire_time = datetime.utcnow() + timedelta(minutes=15)

     to_encode.update({"exp": expire_time})
     encoded_jwt =  jwt.encode(to_encode, SECRET_KEY)
     return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")