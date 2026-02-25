from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.models.booking import Booking
from app.models.fitness_class import FitnessClass
from app.schemas.booking import CreateBookingRequest


async def create_booking(
    db: AsyncSession,
    booking_data: CreateBookingRequest,
    current_user,
):

    result = await db.execute(
        select(FitnessClass).where(
            FitnessClass._id == booking_data.class_id
        )
    )
    fitness_class = result.scalar_one_or_none()

    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")

    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    fitness_class.available_slots -= 1

    new_booking = Booking(
        user_id=current_user._id,
        class_id=fitness_class._id,
    )

    db.add(new_booking)
    db.add(fitness_class)

    await db.commit()
    await db.refresh(new_booking)

    return {
        "id": new_booking._id,
        "class_id": fitness_class._id,
        "class_name": fitness_class.name,
        "start_time": fitness_class.start_time,
        "instructor": fitness_class.instructor,
    }




async def get_user_bookings(
    db: AsyncSession,
    current_user,
):
    result = await db.execute(
        select(Booking)
        .where(Booking.user_id == current_user._id)
        .options(selectinload(Booking.fitness_class))
    )

    bookings = result.scalars().all()

    response = []

    for booking in bookings:
        fitness_class = booking.fitness_class

        response.append({
            "id": booking._id,
            "class_id": fitness_class._id,
            "class_name": fitness_class.name,
            "start_time": fitness_class.start_time,
            "instructor": fitness_class.instructor,
        })

    return response