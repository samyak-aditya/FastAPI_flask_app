from fastapi import APIRouter, HTTPException, Depends
from app.models import UserModel
from app.database import db
from app.auth import hash_password, verify_password

router = APIRouter()

@router.post("/register", response_description="Register a new user")
async def register_user(user: UserModel):
    user_exists = db.users.find_one({"email": user.email})
    if user_exists:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    user.password = hash_password(user.password)
    new_user = db.users.insert_one(user.dict(by_alias=True))
    created_user = db.users.find_one({"_id": new_user.inserted_id})

    return created_user
