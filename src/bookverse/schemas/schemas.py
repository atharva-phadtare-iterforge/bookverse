from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    email: str
    hashedPassword: str

class Author(BaseModel):
    name: str

class Book(BaseModel):
    id: int
    title: str
    isbn: int
    price: int = Field(gt = 0)
    stock: int = Field(ge = 0)
    author: Author

class Order(BaseModel):
    user: User
    status: str
    createdDate: datetime


class OrderItem(BaseModel):
    order: Order
    book: Book
    Quantity: int
    price: int

