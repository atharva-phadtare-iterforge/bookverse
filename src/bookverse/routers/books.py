from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db.db import get_db
from ..models.models import Book as BookModel, Author
from ..schemas.schemas import Book
from ..models.models import Book as BookModel, Author, Review
from ..schemas.schemas import Book, ReviewCreate, ReviewResponse
from ..core.config import get_current_user



router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.get("/")
async def get_books(db: Session = Depends(get_db)):
    books = db.query(BookModel).all()

    return [
        {
            "id": book.id,
            "title": book.title,
            "isbn": book.isbn,
            "price": book.price,
            "stock": book.stock,
            "author": {
                "name": book.author.name,
                "bio": book.author.bio,
            },
        }
        for book in books
    ]


@router.get("/{book_id}")
async def get_book_by_id(
    book_id: int,
    db: Session = Depends(get_db),
):
    book = (
        db.query(BookModel)
        .filter(BookModel.id == book_id)
        .first()
    )

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    return {
        "id": book.id,
        "title": book.title,
        "isbn": book.isbn,
        "price": book.price,
        "stock": book.stock,
        "author": {
            "name": book.author.name,
            "bio": book.author.bio,
        },
    }


@router.post("/")
async def create_book(
    book: Book,
    db: Session = Depends(get_db),
):
    author = (
        db.query(Author)
        .filter(Author.name == book.author.name)
        .first()
    )

    if author is None:
        author = Author(
            name=book.author.name,
            bio=book.author.bio,
        )
        db.add(author)
        db.flush()

    new_book = BookModel(
        title=book.title,
        isbn=book.isbn,
        price=book.price,
        stock=book.stock,
        author_id=author.id,
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return {
        "id": new_book.id,
        "title": new_book.title,
        "isbn": new_book.isbn,
        "price": new_book.price,
        "stock": new_book.stock,
        "author": {
            "name": new_book.author.name,
            "bio": new_book.author.bio,
        },
    }


@router.put("/{book_id}")
async def edit_book(
    book_id: int,
    updated_book: Book,
    db: Session = Depends(get_db),
):
    book = (
        db.query(BookModel)
        .filter(BookModel.id == book_id)
        .first()
    )

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    author = (
        db.query(Author)
        .filter(Author.name == updated_book.author.name)
        .first()
    )

    if author is None:
        author = Author(
            name=updated_book.author.name,
            bio=updated_book.author.bio,
        )
        db.add(author)
        db.flush()

    book.title = updated_book.title
    book.isbn = updated_book.isbn
    book.price = updated_book.price
    book.stock = updated_book.stock
    book.author_id = author.id

    db.commit()
    db.refresh(book)

    return {
        "id": book.id,
        "title": book.title,
        "isbn": book.isbn,
        "price": book.price,
        "stock": book.stock,
        "author": {
            "name": book.author.name,
            "bio": book.author.bio,
        },
    }


@router.delete("/{book_id}")
async def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
):
    book = (
        db.query(BookModel)
        .filter(BookModel.id == book_id)
        .first()
    )

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    deleted_book = {
        "id": book.id,
        "title": book.title,
        "isbn": book.isbn,
        "price": book.price,
        "stock": book.stock,
        "author": {
            "name": book.author.name,
            "bio": book.author.bio,
        },
    }

    db.delete(book)
    db.commit()

    return {
        "message": "Book deleted successfully",
        "book": deleted_book,
    }


@router.post("/{book_id}/reviews", response_model=ReviewResponse)
async def create_review(
    book_id: int,
    review: ReviewCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    book = (
        db.query(BookModel)
        .filter(BookModel.id == book_id)
        .first()
    )

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    new_review = Review(
        book_id=book_id,
        user_id=current_user.id,
        rating=review.rating,
        comment=review.comment,
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review
