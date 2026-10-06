from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class EIn(BaseModel):
    title: str
    date: datetime
    place: str | None = None
    price: float = 0
    capacity: int = 0

@router.post("/")
def create(data: EIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO events (title, date, place, price, capacity)
        VALUES (:title,:date,:place,:price,:capacity) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(upcoming: bool = False, db: Session = Depends(get_session)):
    sql = "SELECT * FROM events"
    if upcoming:
        sql += " WHERE date >= NOW()"
    sql += " ORDER BY date DESC"
    return [dict(r._mapping) for r in db.execute(text(sql)).fetchall()]
