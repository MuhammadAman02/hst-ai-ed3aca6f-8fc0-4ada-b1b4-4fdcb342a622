from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from core.security import get_current_active_user
from models.schemas import User

router = APIRouter()

@router.get("/profile", response_model=User)
async def get_user_profile(current_user: User = Depends(get_current_active_user)):
    """Get current user profile."""
    return current_user

@router.put("/profile", response_model=User)
async def update_user_profile(
    user_update: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update user profile."""
    # Implementation for updating user profile
    # This is a simplified version - in production, you'd want proper validation
    return current_user