from jose import JWTError,jwt
from datetime import datetime,timedelta,timezone
from . import Schemas
from fastapi import Depends,status,HTTPException
from sqlalchemy.orm import Session
from . import database,models
from fastapi.security import OAuth2PasswordBearer
from .config import settings
#SECRET KEY
#ALGORITHM
#EXPIRATION TIME

SECRET_KEY=settings.secret_key
ALGORITHM=settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES=settings.access_token_expire_minutes
oath2_scheme=OAuth2PasswordBearer(tokenUrl='login')
def create_access_token(data:dict):
  to_encode=data.copy()

  expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp":expire})

  encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
  return encoded_jwt

def verify_access_token(token:str,credentials_exception):
  try:
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    id:str=payload.get("id")

    if id is None:
      raise credentials_exception
    token_data=Schemas.TokenData(id=id)
  except JWTError:
    raise credentials_exception
  return token_data
def get_current_user(token:str=Depends(oath2_scheme),db: Session = Depends(database.get_db)):
  credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate Credentials")
  token_data=verify_access_token(token,credentials_exception)
  user=db.query(models.User).filter(models.User.id==token_data.id).first()
  if not user:
    raise credentials_exception
  return user

