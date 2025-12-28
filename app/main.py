from fastapi import FastAPI
from app.db.session import lifespan
import app.db.models

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"status": True, "message": "App running"}
