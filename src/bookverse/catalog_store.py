from pathlib import Path
import json
import logging

from .schemas.schemas import Book


PACKAGE_BOOKS_FILE = Path(__file__).parent / "books.json"


class InvalidBookError(Exception):
    pass


logging.basicConfig(
    filename="message.log",
    format="%(asctime)s: %(levelname)s: %(message)s",
    level=logging.INFO,
)


def _get_books_file() -> Path:
    current_directory_file = Path.cwd() / "books.json"

    if current_directory_file.exists():
        return current_directory_file

    return PACKAGE_BOOKS_FILE


def validate_book(book):
    if not book.get("title"):
        raise InvalidBookError("Book title is required")

    if not book.get("author"):
        raise InvalidBookError("Book author is required")

    if book.get("price") is None or book["price"] <= 0:
        raise InvalidBookError(
            "Book price must be greater than 0"
        )

    if book.get("stock") is None or book["stock"] < 0:
        raise InvalidBookError(
            "Book stock cannot be negative"
        )


def load_catalog():
    books_file = _get_books_file()

    with open(books_file, "r", encoding="utf-8") as file:
        books = json.load(file)

    for book in books:
        validate_book(book)
        Book.model_validate(book)

    return books


def save_catalog(books):
    books_file = _get_books_file()

    with open(books_file, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)
