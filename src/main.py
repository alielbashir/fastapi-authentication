from fastapi import FastAPI

app = FastAPI()

users = []


@app.post("/register")
def register():
    return {}


@app.post("/login")
def login():
    return {}


@app.post("/unprotected")
def unprotected():
    return {"hello": "world"}


@app.post("/protected")
def protected():
    return {}
