from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import database,models,oath2,Schemas
router=APIRouter(prefix="/vote",tags=['Vote'])

@router.post("/",status_code=201)
def vote(vote:Schemas.Vote,db:Session=Depends(database.get_db),current_user=Depends(oath2.get_current_user)):
  post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
  if not post:
    raise HTTPException(status_code=404,detail=f"NO POST FOUND WITH THE ID {vote.post_id}")
  vote_query=db.query(models.Votes).filter(models.Votes.post_id==vote.post_id,models.Votes.user_id==current_user.id)
  if vote.dir==1:
    if vote_query.first():
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Already Voted for this post")
    post=models.Votes(post_id=vote.post_id,user_id=current_user.id)
    db.add(post)
    db.commit()
    return {"message":"Succesfully added vote"}
  else:
    if not vote_query.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Vote not found")
    db.delete(vote_query.first())
    db.commit()
    return {"Message":"Vote Deleted Succesfully"}



