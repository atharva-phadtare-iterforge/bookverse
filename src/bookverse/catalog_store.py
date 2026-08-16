import json
import logging
from .schemas import Book, Order


class InvalidBookError(Exception):
    pass

logging.basicConfig(filename="message.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.INFO)

def validate_book(book):
    if not book.get("title"):
        raise InvalidBookError("Book title is required")

    if not book.get("author"):
        raise InvalidBookError("Book author is required")

    if book.get("price") is None or book["price"] <= 0:
        raise InvalidBookError("Book price must be greater than 0")

    if book.get("stock") is None or book["stock"] < 0:
        raise InvalidBookError("Book stock cannot be negative")


def load_catalog():
    with open("books.json", "r") as f:
        books = json.load(f)

    for book in books:
        Book.model_validate(book)

    return books


def save_catalog():
    books = load_catalog()

    books.append({
        "title": "ABC",
        "author": {
            "name": "Robert Kiyosaki"
        },
        "price": 29,
        "stock": 11
    })

    with open("books.json", "w") as f:
        json.dump(books, f, indent=4)


try:
    books = load_catalog()

    for book in books:
        print(book)

    save_catalog()

except InvalidBookError as e:
    import json
import logging


class InvalidBookError(Exception):
    pass

logging.basicConfig(filename="message.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    level=logging.INFO)

def validate_book(book):
    if not book.get("title"):
        raise InvalidBookError("Book title is required")

    if not book.get("author"):
        raise InvalidBookError("Book author is required")

    if book.get("price") is None or book["price"] <= 0:
        raise InvalidBookError("Book price must be greater than 0")

    if book.get("stock") is None or book["stock"] < 0:
        raise InvalidBookError("Book stock cannot be negative")


def load_catalog():
    with open("books.json", "r") as f:
        books = json.load(f)

    for book in books:
        validate_book(book)

    return books


def save_catalog():
    books = load_catalog()

    books.append({
        "title": "ABC",
        "author": "Robert Kiyosaki",
        "price": 29,
        "stock": 11
    })

    with open("books.json", "w") as f:
        json.dump(books, f, indent=4)


try:
    books = load_catalog()

    for book in books:
        print(book)

    save_catalog()

except InvalidBookError as e:
    logging.error(e)