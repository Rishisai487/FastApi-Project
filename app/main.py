from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from . import models
from .database import engine
from .routers import post,user,auth,vote
from fastapi.middleware.cors import CORSMiddleware
# # create tables
# models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get('/')
def soemthing():
  return {"msg": "ok"}

# List of allowed origins
origins = [
"https://www.google.com",
"https://youtube.com"
]
# Adding CORSMiddleware to the FastAPI application
app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # List of allowed origins
allow_credentials=True, # Allow credentials such as cookies and authorization headers
allow_methods=["*"], # Allow all HTTP methods
allow_headers=["*"], # Allow all HTTP headers
)

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)
app.include_router(vote.router)