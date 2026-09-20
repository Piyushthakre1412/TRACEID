from fastapi import APIRouter, HTTPException
from app.db.loader import get_profile_by_id

router = APIRouter()

@router.get("/profile/{person_id}")
async def get_profile(person_id: str):
    """GET /api/profile/{id} - Fetches detailed profile metadata."""
    profile = get_profile_by_id(person_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Identity profile not found")
    return profile
