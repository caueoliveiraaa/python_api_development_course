from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message":"System operating successfully."}


@app.get("/posts")
def get_posts():
    return {"data": "These are your posts"}
