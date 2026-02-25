from typing import List
import logging
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.fitness_class import CreateClassRequest, ClassResponse
from app.core.dependencies import get_db, get_current_user
from app.models.user import User
from app.apis.fitness_class.controller import (
    get_all_upcoming_classes,
    add_new_fitness_class
)

router = APIRouter(tags=["classes"])
logger = logging.getLogger(__name__)

@router.get("/classes", response_model=List[ClassResponse])
async def fetch_upcoming_classes(
    db: AsyncSession = Depends(get_db)
):
    logging.info("Get all upcoming fitness classes.")
    result = await get_all_upcoming_classes(db)
    return [
    {
        "id": r._id,
        "name": r.name,
        "instructor": r.instructor,
        "start_time": r.start_time,
        "available_slots": r.available_slots,
    }
    for r in result
]


@router.post("/classes", response_model=ClassResponse)
async def create_new_class(
    fitness_class: CreateClassRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    logging.info("Add a new class.")
    result = await add_new_fitness_class(db, fitness_class, current_user)
    return {
    "id": result._id,
    "name": result.name,
    "instructor": result.instructor,
    "start_time": result.start_time,
    "available_slots": result.available_slots,
    }