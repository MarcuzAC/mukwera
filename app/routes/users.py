from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.database import get_supabase
from typing import List

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.get("/", response_model=List[dict])
async def get_users(token: str = Depends(oauth2_scheme)):
    supabase = get_supabase()
    users = supabase.table("users").select("*").execute()
    return users.data

@router.get("/{user_id}")
async def get_user(user_id: str, token: str = Depends(oauth2_scheme)):
    supabase = get_supabase()
    user = supabase.table("users").select("*").eq("id", user_id).execute()
    if not user.data:
        raise HTTPException(status_code=404, detail="User not found")
    return user.data[0]