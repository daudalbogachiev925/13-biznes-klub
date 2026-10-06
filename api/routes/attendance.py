from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class AIn(BaseModel):
    member_id: int
    event_id: int

@router.post("/")
def mark(data: AIn, db: Session = Depends(get_session)):
    db.execute(text("""
        INSERT INTO attendance (member_id, event_id) VALUES (:member_id, :event_id)
        ON CONFLICT DO NOTHING
    """), data.dict())
    db.commit()
    return {"status": "marked"}

@router.get("/event/{event_id}")
def by_event(event_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT m.name, m.tier FROM attendance a
        JOIN members m ON m.id = a.member_id
        WHERE a.event_id = :e
    """), {"e": event_id}).fetchall()]
