from sqlalchemy.orm import Session
from app.models import User

def get_user_for_login(db: Session, user_id: str, name: str, password: str):
    return db.query(User).filter(
        User.user_id == user_id,
        User.name == name,
        User.password == password
    ).first()

