from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class MIn(BaseModel):
    name: str
    email: str | None = None
    phone: str | None = None
    tier: str
    monthly_fee: float

@router.post("/")
def create(data: MIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO members (name, email, phone, tier, monthly_fee)
        VALUES (:name,:email,:phone,:tier,:monthly_fee) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(tier: str | None = None, db: Session = Depends(get_session)):
    sql = "SELECT * FROM members WHERE status='active'"
    params = {}
    if tier:
        sql += " AND tier = :t"
        params['t'] = tier
    return [dict(r._mapping) for r in db.execute(text(sql), params).fetchall()]

@router.get("/{member_id}")
def get(member_id: int, db: Session = Depends(get_session)):
    m = db.execute(text("SELECT * FROM members WHERE id=:i"), {"i": member_id}).fetchone()
    if not m: raise HTTPException(404)
    return dict(m._mapping)

@router.post("/{member_id}/cancel")
def cancel(member_id: int, db: Session = Depends(get_session)):
    db.execute(text("UPDATE members SET status='cancelled' WHERE id=:i"), {"i": member_id})
    db.commit()
    return {"status": "cancelled"}
