from fastapi import FastAPI
from routes import members, events, attendance, payments, reports

app = FastAPI(title="Business Club API")
app.include_router(members.router, prefix="/members", tags=["members"])
app.include_router(events.router, prefix="/events", tags=["events"])
app.include_router(attendance.router, prefix="/attendance", tags=["attendance"])
app.include_router(payments.router, prefix="/payments", tags=["payments"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.get("/health")
def health(): return {"status": "ok"}
