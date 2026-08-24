from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..core.config import create_access_token
from ..db.db import get_db
from ..models.models import User
from ..schemas.schemas import UserCreate, UserResponse


router = APIRouter()

password_hash = PasswordHash.recommended()


@router.post("/register", response_model=UserResponse)
async def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = db.scalar(
        select(User).where(User.email == user_data.email)
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    hashed_password = password_hash.hash(
        user_data.password
    )

    new_user = User(
        email=user_data.email,
        hashed_password=hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login")
async def login(
    user_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    valid_user = db.scalar(
        select(User).where(
            User.email == user_data.username
        )
    )

    if not valid_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    password_valid = password_hash.verify(
        user_data.password,
        valid_user.hashed_password,
    )

    if not password_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(valid_user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
