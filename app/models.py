from sqlalchemy import Column, String
from app.database import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(String, primary_key=True, index=True)  # 학번
    name = Column(String, nullable=False)                   # 이름
    password = Column(String, nullable=False)               # 비밀번호
