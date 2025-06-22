from fastapi import HTTPException

from fastapi import routing, FastAPI

from FileUpload.crud import create_user, authenticate_user
from FileUpload.schemas import UserCreate, UserLogin
from auth.JWTmain import create_access_token

router_user = FastAPI()

@router_user.post("/signup", response_model=UserCreate)
def creating_user(user : UserCreate):
    try :
        create_user(user)
    except :
        raise HTTPException(status_code=401,deatil="Invalid username or password provided")


@router_user.get("/login", response_model=UserLogin)
def login_user(user : UserLogin):
    try :
        authenticate_user(user)
        jwt_token = create_access_token({"sub" : user.username})
        return jwt_token
    except :
        raise HTTPException(status_code=401,deatil="Invalid username or password provided")


