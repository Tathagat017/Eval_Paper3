from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.services.rag_service import rag_chain
from app.schemas import UserResponseRequest

app = APIRouter()

@app.post("/user/register", response_model=UserResponseRequest)
async def register(db:get_db,user:UserCreateRequest):
    try:
     pass
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))