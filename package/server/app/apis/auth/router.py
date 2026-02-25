from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserSignupRequest, UserLoginRequest, UserResponse
from app.schemas.auth import TokenResponse
from app.core.dependencies import get_db
from app.apis.auth.controller import (
    register_user,
    authenticate_user
)
import logging
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["auth"])
logger = logging.getLogger(__name__)

@router.post("/signup", response_model=UserResponse)
async def register(
    user: UserSignupRequest,
    db: AsyncSession = Depends(get_db),
):
    logging.info("Register attempt for email.")
    return await register_user(db, user)




@router.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    _, token = await authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }