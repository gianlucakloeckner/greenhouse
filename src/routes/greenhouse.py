from fastapi import APIRouter, Depends
from src.models.greenhouse import Greenhouse
from src.models.users import User
from src.handlers.users import get_current_active_user
from src.handlers.greenhouses import GreenhouseManager

router = APIRouter()


@router.post("/greenhouse/")
async def create_greenhouse(greenhouse: Greenhouse, current_user: User = Depends(get_current_active_user)):
    greenhouse.user_email = current_user.email
    g = GreenhouseManager()
    status = g.create_greenhouse(greenhouse)
    if status:
        return g.get_greenhouse(greenhouse.id)
    else:
        return {"message": "failed"}


@router.get("/greenhouse/{greenhouse_id}")
async def get_greenhouse(greenhouse_id: str, current_user: User = Depends(get_current_active_user)):
    g = GreenhouseManager()
    greenhouse = g.get_greenhouse(greenhouse_id)
    if greenhouse:
        return greenhouse
    else:
        return {"message": "Greenhouse not found"}


@router.put("/greenhouse/{greenhouse_id}")
async def update_greenhouse(greenhouse_id: str, greenhouse: Greenhouse, current_user: User = Depends(get_current_active_user)):
    g = GreenhouseManager()
    status = g.update_greenhouse(greenhouse_id, greenhouse.dict())
    if status:
        return g.get_greenhouse(greenhouse_id)
    else:
        return {"message": "failed"}


@router.delete("/greenhouse/{greenhouse_id}")
async def delete_greenhouse(greenhouse_id: str, current_user: User = Depends(get_current_active_user)):
    g = GreenhouseManager()
    status = g.delete_greenhouse(greenhouse_id)
    if status:
        return {"message": "Greenhouse deleted successfully"}
    else:
        return {"message": "failed"}


@router.get("/greenhouses/")
async def get_all_greenhouses(current_user: User = Depends(get_current_active_user)):
    g = GreenhouseManager()
    greenhouses = g.get_all_greenhouses()
    return greenhouses
