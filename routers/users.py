from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from views.users import get_users
from models.database import get_db
from models import schemas


router = APIRouter()


@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users
