from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)


class UserResponse(BaseModel):
    id: int
    email: EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Author(BaseModel):
    name: str


class Book(BaseModel):
    id: int
    title: str
    isbn: int
    price: Decimal = Field(gt=0)
    stock: int = Field(ge=0)
    author: Author


class OrderItemCreate(BaseModel):
    book_id: int
    quantity: int = Field(gt=0)


class OrderCreate(BaseModel):
    items: list[OrderItemCreate] = Field(min_length=1)


class OrderResponse(BaseModel):
    id: int
    user_id: int
    status: str
    created_date: date


class OrderItemResponse(BaseModel):
    id: int
    book_id: int
    quantity: int
    price: Decimal


class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    comment: str | None = None


class ReviewResponse(BaseModel):
    id: int
    book_id: int
    user_id: int
    rating: int
    comment: str | None = None