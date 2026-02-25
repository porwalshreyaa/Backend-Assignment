from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from datetime import datetime, timedelta
from jose import jwt

from app.models.user import User
from app.schemas.user import UserSignupRequest
from app.core.security import hash_password, verify_password
from app.core.config import settings

async def register_user(
    db: AsyncSession,
    user_data: UserSignupRequest,
):

    result = await db.execute(
        select(User).where(User.email == user_data.email)
    )
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hash_password(user_data.password),
    )

    db.add(new_user)

    await db.commit()
    await db.refresh(new_user)

    return {
        "id": new_user._id,
        "name": new_user.name,
        "email": new_user.email
    }


async def authenticate_user(
    db: AsyncSession,
    email: str,
    password: str,
):
    result = await db.execute(
        select(User).where(User.email == email)
    )

    db_user = result.scalar_one_or_none()

    if not db_user or not verify_password(password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token_for_user(db_user)

    return db_user, token


def create_access_token_for_user(user: User):
    expire = datetime.now(tz=ZoneInfo('Asia/Kolkata')) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user._id),
        "exp": expire,
    }

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    return token