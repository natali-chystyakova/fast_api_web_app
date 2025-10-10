from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.database import get_db
from models import schemas
from controllers.tokens import create_tokens


router = APIRouter()


@router.post("", response_model=schemas.Token, status_code=201)
def create_token(user_data: schemas.UserAuth, db: Session = Depends(get_db)):
    return create_tokens(db=db, user_data=user_data)
