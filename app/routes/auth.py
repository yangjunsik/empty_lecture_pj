from fastapi import APIRouter, Form
from database.db import get_db
from services.jwt_handler import create_token

router = APIRouter()

@router.post("/login")
def login(student_id: str = Form(...), name: str = Form(...), phone: str = Form(...)):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM users
        WHERE student_id = ? AND name = ? AND phone = ?
    """, (student_id, name, phone))
    user = cur.fetchone()
    conn.close()

    if user:
        token = create_token(user_id=student_id)
        return {"success": True, "token": token}
    else:
        return {"success": False, "message": "로그인 실패"}