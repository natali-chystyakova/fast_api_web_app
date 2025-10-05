from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from views.users import get_users
from models.database import get_db
from models import schemas
from controllers.users import register


router = APIRouter()


@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("", response_model=schemas.LiteUser, status_code=201)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return register(db=db, user_data=user_data)
