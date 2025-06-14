""" Entry point of the application """
from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


@app.get("/")
def root():
    """ Root endpoint """
    return {"message":"System operating successfully"}


@app.get("/posts")
def get_posts():
    """ Fetch posts """
    return {"data": "These are your posts"}


@app.post("/createposts")
def get_post(payload: dict = Body):
    """ Generate new posts """
    print(payload)
    return {"message": "sucessfully created post"}
