from cmath import log
from src import crud
from .utils.hashing import verify_password
from sqlalchemy.orm import Session

# ==== AUTH ====

def authenticate_user(db: Session, email: str, password: str):
    user = crud.get_user_by_email(db, email)
    if not user:
        return 1
    if not verify_password(password, user.hashed_password):
        return 2
    return user