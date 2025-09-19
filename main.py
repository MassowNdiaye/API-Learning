from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body #fastapi.params = the internal module where Body is defined.  / Body = tells FastAPI a parameter should come from the request body (usually JSON on PostMan).
from pydantic import BaseModel #pydantic = It validates incoming request data automatically (e.g., types, required fields).


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional [int] = None



@app.get("/") 
# The "/" is used to indicate the type of URL in this case http://127.0.0.1:8000/, if I write "/login" the would be http://127.0.0.1:8000/login.
# @ = decorator.
# app = FastAPI() -> Line 2.
# get = Used to retrive data from a server. HTTP Method
def root(): 
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.model_dump()) # .model_dump() = new recommended method in Pydantic v2. replace .dict
    return {"data": "new_post"}
# title str, content str