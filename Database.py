from sqlalchemy import create_engine
from sqlmodel import SQLModel

MYSQL_URL = "mysql+pymysql://root:password@localhost:3306/file_upload_db"

engine = create_engine(MYSQL_URL,echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)