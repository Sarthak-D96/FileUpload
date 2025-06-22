#file uploading routers
# first, lets add the authentication system

from fastapi import HTTPException
from fastapi import routing, FastAPI
from fastapi.params import Depends
from sqlmodel import Session, select
from FileUpload.Database import engine
from FileUpload.config import store_file
from fastapi import UploadFile
from FileUpload.jwt_handling import get_current_user
from FileUpload.models import UploadedFile, User
from FileUpload.router.user_router import login_user


router_file = FastAPI()


@router_file.post("/upload")
def uploading_files(file : UploadFile, current_user: dict = Depends(get_current_user) ):
    try:
        store_file(file)
        with Session(engine) as session:
            statement = select(User).where(User.username == current_user["username"])
        notify_user = session.exec(statement).first()
        # this notify_user can be employed in further utilities such as:
        # informing users about their upload etc etc.

    except:
        raise HTTPException(status_code=404,detail="Some error occurred while uploading the file")