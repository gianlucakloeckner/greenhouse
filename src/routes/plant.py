from fastapi import APIRouter, Depends, HTTPException
from src.models.plant import Plant
from src.models.users import User
from src.handlers.users import get_current_active_user
from src.handlers.plants import PlantManager

router = APIRouter()


@router.post("/greenhouse/{greenhouse_id}/plant/")
async def create_plant(greenhouse_id: str, plant: Plant, current_user: User = Depends(get_current_active_user)):
    plant.greenhouse_id = greenhouse_id
    p = PlantManager()
    status = p.create_plant(plant)
    if status:
        return p.get_plant(plant.id)
    else:
        raise HTTPException(status_code=400, detail="Plant creation failed")


@router.get("/plant/{plant_id}")
async def get_plant(plant_id: str, current_user: User = Depends(get_current_active_user)):
    p = PlantManager()
    plant = p.get_plant(plant_id)
    if plant:
        return plant
    else:
        raise HTTPException(status_code=404, detail="Plant not found")


@router.put("/plant/{plant_id}")
async def update_plant(plant_id: str, plant: Plant, current_user: User = Depends(get_current_active_user)):
    p = PlantManager()
    status = p.update_plant(plant_id, plant)
    if status:
        return p.get_plant(plant_id)
    else:
        raise HTTPException(status_code=400, detail="Plant update failed")


@router.delete("/plant/{plant_id}")
async def delete_plant(plant_id: str, current_user: User = Depends(get_current_active_user)):
    p = PlantManager()
    status = p.delete_plant(plant_id)
    if status:
        return {"message": "Plant deleted successfully"}
    else:
        raise HTTPException(status_code=400, detail="Plant deletion failed")


@router.get("/greenhouse/{greenhouse_id}/plants/")
async def get_plants_by_greenhouse(greenhouse_id: str, current_user: User = Depends(get_current_active_user)):
    p = PlantManager()
    plants = p.get_plants_by_greenhouse(greenhouse_id)
    return plants
