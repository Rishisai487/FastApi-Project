
from fastapi import FastAPI, Response, status, HTTPException, Depends,APIRouter
from typing import List,Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models,Schemas
from app.database import engine,get_db
from .. import oath2
# create tables
router=APIRouter(prefix="/posts",tags=["Posts"])
@router.get("/",response_model=List[Schemas.PostOut])
def get_posts(db:Session=Depends(get_db),current_user = Depends(oath2.get_current_user),limit:int=15,skip:int=0,search:Optional[str]=""):
    posts=db.query(models.Post,func.count(models.Votes.post_id).label("likes")).outerjoin(models.Votes,models.Post.id==models.Votes.post_id).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts
@router.post("/",response_model=Schemas.PostResponse)
def create_post(Post:Schemas.PostCreate,db:Session=Depends(get_db),current_user=Depends(oath2.get_current_user)):
    created_post=models.Post(**Post.model_dump(),owner_id=current_user.id)
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post
@router.get("/{id}",response_model=Schemas.PostOut)
def get_post(id:int,db:Session=Depends(get_db),current_user=Depends(oath2.get_current_user)):
    returned_post=db.query(models.Post,func.count(models.Votes.post_id).label("likes")).outerjoin(models.Votes,models.Post.id==models.Votes.post_id).group_by(models.Post.id).filter(models.Post.id==id).first()
    if not returned_post:
        raise HTTPException(status_code=404,detail=f"Post not found with id {id}")
    return returned_post
@router.delete("/{id}",status_code=status.HTTP_200_OK)
def delete_post(id:int,db:Session=Depends(get_db),current_user=Depends(oath2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=404,detail=f"Post not found with id {id}")
    elif post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not able to delete this post")
    db.delete(post)
    db.commit()
@router.put("/{id}",response_model=Schemas.PostResponse)
def update_post(id:int,request:Schemas.PostUpdate,db=Depends(get_db),current_user=Depends(oath2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id==id)
    if not post.first():
        raise HTTPException(status_code=404,detail=f"Post not found with id {id}")
    if post.first().owner_id!=current_user.id:
        raise HTTPException(status_code=403,detail="You Cant Update others posts!")
    post.update(request.model_dump(),synchronize_session=False)
    db.commit()
    return post.first()