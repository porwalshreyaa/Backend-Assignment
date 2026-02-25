from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from datetime import datetime
import pytz

from app.models.fitness_class import FitnessClass
from app.schemas.fitness_class import CreateClassRequest


async def get_all_upcoming_classes(db: AsyncSession):
    now_ist = datetime.now(tz=ZoneInfo('Asia/Kolkata'))

    result = await db.execute(
                select(FitnessClass)
                .where(FitnessClass.start_time >= now_ist)
                .order_by(FitnessClass.start_time.asc())
            )

    classes = result.scalars().all()

    return classes


async def add_new_fitness_class(
    db: AsyncSession,
    fitness_class: CreateClassRequest,
    current_user,
):


    new_class = FitnessClass(
        name=fitness_class.name,
        instructor=fitness_class.instructor,
        start_time=fitness_class.start_time,
        available_slots=fitness_class.available_slots,
    )

    db.add(new_class)
    await db.commit()
    await db.refresh(new_class)

    return new_class