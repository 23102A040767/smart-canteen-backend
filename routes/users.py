from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserCreate

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    
    new_user = User(
    name=user.name,
    email=user.email,
    password=user.password,
    role="consumer"
)
    db.add(new_user)
    db.commit()

    return {"message": "User Registered Successfully"}