from warnings import deprecated
from passlib.context import CryptContext


SECRET_KEY = "afd76b951c069dccb9ef88cb55232844e663e4c5e5fcf6df4400808f29962166"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


