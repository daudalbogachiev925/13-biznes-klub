from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class PIn(BaseModel):
    member_id: int
    amount: float
    kind: str = 'monthly'

@router.post("/")
def create(data: PIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO payments (member_id, amount, kind)
        VALUES (:member_id, :amount, :kind) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/member/{member_id}")
def by_member(member_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT * FROM payments WHERE member_id=:m ORDER BY paid_at DESC
    """), {"m": member_id}).fetchall()]
