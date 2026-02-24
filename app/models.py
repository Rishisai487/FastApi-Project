from .database import Base
from sqlalchemy import Column,Integer,String,Boolean, text,ForeignKey
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import relationship
class Post(Base):
  __tablename__="posts"
  id=Column(Integer,primary_key=True,nullable=False)
  title=Column(String,nullable=False)
  content=Column(String,nullable=False) 
  published=Column(Boolean,nullable=False,server_default=text("TRUE"))
  created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
  owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
  owner=relationship("User")
  votes=relationship("Votes")
class User(Base):
  __tablename__="users"
  id=Column(Integer,nullable=False,primary_key=True)
  username=Column(String,nullable=False,unique=True)
  email=Column(String,nullable=False,unique=True)
  password=Column(String,nullable=False)
  created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
  role=Column(String,nullable=False,server_default='user')
  phone_no=Column(String)

class Votes(Base):
  __tablename__="votes"
  post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True,nullable=False)
  user_id=Column(Integer,ForeignKey("users.id"),primary_key=True,nullable=False)
  

  
