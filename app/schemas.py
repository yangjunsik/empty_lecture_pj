from pydantic import BaseModel

class UserLogin(BaseModel):
    user_id: str
    name: str
    password: str
