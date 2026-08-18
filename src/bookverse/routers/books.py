from fastapi import APIRouter, HTTPException

from ..catalog_store import load_catalog, save_catalog
from ..schemas.schemas import Book


router = APIRouter(
    prefix="/books",
    tags=["Books"]
)


@router.get("/")
async def get_books():
    return load_catalog()


@router.get("/{book_id}")
async def get_book_by_id(book_id: int):
    books = load_catalog()

    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


@router.post("/")
async def create_book(book: Book):
    books = load_catalog()

    new_id = max(
        [book["id"] for book in books],
        default=-1
    ) + 1

    new_book = Book(
        id=new_id,
        title=book.title,
        isbn=book.isbn,
        price=book.price,
        stock=book.stock,
        author=book.author
    )

    books.append(new_book.model_dump())
    save_catalog(books)

    return new_book


@router.put("/{book_id}")
async def edit_book(book_id: int, updated_book: Book):
    books = load_catalog()

    for index, book in enumerate(books):
        if book["id"] == book_id:
            updated_book.id = book_id
            books[index] = updated_book.model_dump()

            save_catalog(books)

            return books[index]

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


@router.delete("/{book_id}")
async def delete_book(book_id: int):
    books = load_catalog()

    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted_book = books.pop(index)

            save_catalog(books)

            return {
                "message": "Book deleted successfully",
                "book": deleted_book
            }

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )