from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


@app.get("/")
def root():
    return {"message":"System operating successfully"}


@app.get("/posts")
def get_posts():
    return {"data": "These are your posts"}


@app.post("/createposts")
def get_post(payload: dict = Body):
    return {"message": "sucessfully created post"}
    