# logic for storing files and uploading their status in DB

import os
from datetime import datetime
from fastapi import HTTPException
from importlib.resources import contents

from fastapi import UploadFile
import shutil

UPLOAD_DIR = "uploaded files path"

def store_file(file : UploadFile):

    #univervsal file checking system
    # for a file named 'file'
    file.file.seek(0, os.SEEK_END)
    file_size = file.file.tell()
    file.file.seek(0)

    if file_size > 5 * 1024 * 1024: # 5 here can be replaced with any number (*1024*1024) here stands for MB
        raise HTTPException(status_code=400, detail="File too large")

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    return {"file stored at:" : file_path}