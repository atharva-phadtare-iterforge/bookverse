from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.config import get_current_user
from ..db.db import get_db
from ..models.models import Book, Order, OrderItem, User
from ..schemas.schemas import OrderCreate, OrderResponse


router = APIRouter()


@router.post("/orders", response_model=OrderResponse)
async def create_order(
    order_data: OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    validated_items = []

    for item in order_data.items:
        book = db.get(Book, item.book_id)

        if book is None:
            raise HTTPException(
                status_code=404,
                detail=f"Book {item.book_id} not found",
            )

        if book.stock < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Not enough stock for {book.title}",
            )

        validated_items.append((item, book))

    new_order = Order(
        user_id=current_user.id,
        status="Created",
        created_date=date.today(),
    )

    db.add(new_order)
    db.flush()

    for item, book in validated_items:
        order_item = OrderItem(
            order_id=new_order.id,
            book_id=book.id,
            quantity=item.quantity,
            price=book.price,
        )

        book.stock -= item.quantity

        db.add(order_item)

    db.commit()
    db.refresh(new_order)

    return new_order

@router.get("/me")
async def get_my_orders(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    orders = (
        db.query(Order)
        .filter(Order.user_id == current_user.id)
        .order_by(Order.created_date.desc())
        .all()
    )

    return orders

