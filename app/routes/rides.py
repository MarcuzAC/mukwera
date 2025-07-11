from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.database import get_supabase
from app.models import RideCreate
from typing import List

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/request")
async def request_ride(ride: RideCreate, token: str = Depends(oauth2_scheme)):
    supabase = get_supabase()
    
    # Verify user exists
    user = supabase.table("users").select("*").eq("id", ride.user_id).execute()
    if not user.data:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Create ride
    new_ride = supabase.table("rides").insert({
        "user_id": ride.user_id,
        "pickup_lat": ride.pickup_lat,
        "pickup_lng": ride.pickup_lng,
        "destination_lat": ride.destination_lat,
        "destination_lng": ride.destination_lng,
        "status": "requested"
    }).execute()
    
    return {"message": "Ride requested", "ride_id": new_ride.data[0]["id"]}

@router.get("/active")
async def get_active_rides(token: str = Depends(oauth2_scheme)):
    supabase = get_supabase()
    rides = supabase.table("rides").select("*").eq("status", "requested").execute()
    return rides.data