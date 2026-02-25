from typing import List
import logging
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.booking import CreateBookingRequest, BookingResponse
from app.core.dependencies import get_db, get_current_user
from app.models.user import User
from app.apis.bookings.controller import (
    create_booking,
    get_user_bookings,
)

router = APIRouter( tags=["bookings"])
logger = logging.getLogger(__name__)


@router.post("/book", response_model=BookingResponse)
async def book_class(
    booking: CreateBookingRequest,
    db: AsyncSession = Depends(get_db), 
    current_user: User = Depends(get_current_user),
):
    logging.info("Book Session attempt.")
    booking = await create_booking(db, booking, current_user)
    return booking


@router.get("/bookings", response_model=List[BookingResponse])
async def fetch_my_bookings(
    db: AsyncSession = Depends(get_db), 
    current_user: User = Depends(get_current_user),
):
    logging.info("List all Bookings for a user.")
    bookings = await get_user_bookings(db, current_user)
    return bookings