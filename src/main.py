from fastapi import Depends, FastAPI, HTTPException

from .auth import AuthHandler
from .schema import AuthDetails

app = FastAPI()

auth_handler = AuthHandler()
users = []


@app.post("/register", status_code=201)
def register(auth_details: AuthDetails):
    if any(x["username"] == auth_details.username for x in users):
        # if name is taken
        raise HTTPException(status_code=400, detail="Username is taken")
    hashed_pass = auth_handler.get_password_hash(auth_details.password)
    users.append({"username": auth_details.username, "password": hashed_pass})
    return


@app.post("/login")
def login(auth_details: AuthDetails):
    user = None
    for x in users:
        if x["username"] == auth_details.username:
            user = x
            break

    if user is None or not auth_handler.verify_password(
        auth_details.password, user["password"]
    ):
        raise HTTPException(status_code=401, detail="Invalid username and/or password")
    token = auth_handler.encode_token(user["username"])

    return {"token": token}


@app.post("/unprotected")
def unprotected():
    return {"hello": "world"}


@app.post("/protected")
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {"name": username}
