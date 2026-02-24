from fastapi import FastAPI, Response, status, HTTPException, Depends,APIRouter
from typing import List
from sqlalchemy.orm import Session
from .. import models,Schemas,oath2
from app.database import engine,get_db
from app.utils import hash
# create tables
router=APIRouter(prefix="/users",tags=["Users"])
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=Schemas.CreationResponse)
def create_user(Data:Schemas.Creation,db=Depends(get_db)):
    try:
        #hash the password
        Data.password=hash(Data.password)
        user=models.User(**Data.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email or username already exists")

@router.get("/{id}",response_model=Schemas.CreationResponse)
def get_user(id:int,db:Session=Depends(get_db),current_user=Depends(oath2.get_current_user)):
    details=db.query(models.User).filter(models.User.id==id).first()
    if not details:
        raise HTTPException(status_code=404,detail=f"User not Found with the ID {id}")
    return details
@router.get("/",response_model=list[Schemas.CreationResponse])
def get_users(db:Session=Depends(get_db),current_user=Depends(oath2.get_current_user)):
    if current_user.role!='admin':
        raise HTTPException(status_code=403,detail=f"You are Forbidden from this task!!")
    details=db.query(models.User).filter().all()
    if not details:
        raise HTTPException(status_code=404,detail=f"No users ! !")
    return details