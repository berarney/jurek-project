from fastapi import APIRouter
from models.models import UserSchema, PostSchema, UserLoginSchema
from config.database import collection_name
from schemas.schemas import list_serial
from bson import objectid
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()



from fastapi import FastAPI, Body, Depends
from FastAPI.handler import signJWT
from FastAPI.bearer import Bearer
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
users = []
posts = [
    {
        "title": "Cats",
        "description": "All about cats.",
        "author": "Rimma"
    }
]


@router.get("/")
def root():
    return {"message": "Hello World"}

def verify_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@router.get("/")
async def get_edus():
    edus = list_serial(collection_name.find())
    return edus

@router.post("/posts", dependencies=[Depends(Bearer())])
def create_post(post: PostSchema = Body(...)):
    posts.append(post)
    return post

@router.post("/user/signup")
def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)

@router.post("/user/signin")
def login_user(user: UserLoginSchema = Body(...)):
    if verify_user(user):
        return signJWT(user.email)
    return {"error": "Invalid credentials :("}

