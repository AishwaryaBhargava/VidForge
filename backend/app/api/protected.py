from fastapi import APIRouter, Depends
from app.core.auth import get_current_user

router = APIRouter()

@router.get("/me")
def read_current_user(current_user=Depends(get_current_user)):
    return {
        "uid": current_user["uid"],
        "email": current_user["email"],
    }
