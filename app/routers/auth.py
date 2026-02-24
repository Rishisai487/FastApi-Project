from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import Schemas,utils,models,oath2

router=APIRouter(tags=['Authentication'])
@router.post('/login',response_model=Schemas.Token)
def login(credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
  row=db.query(models.User).filter(models.User.email==credentials.username).first()
  if not row:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Incorrect Email or Password")
  if utils.verify(credentials.password,row.password):
    access_token=oath2.create_access_token(data={"id":row.id})
    return {"access_token":access_token,"token_type":"bearer"}
  raise HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Incorrect email or password"
)
