from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

@router.get("/revenue")
def revenue(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/revenue.sql').read())).fetchall()]

@router.get("/churn")
def churn(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/churn.sql').read())).fetchall()]

@router.get("/events")
def events_report(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/events.sql').read())).fetchall()]
