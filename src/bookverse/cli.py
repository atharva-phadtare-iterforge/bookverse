import argparse

from .schemas.schemas import Book, Author
from .catalog_store import (
    load_catalog,
    save_catalog,
    InvalidBookError,
)


def add_book(args):
    books = load_catalog()

    for book in books:
        if book.get("isbn") == args.isbn:
            print("Book already exists.")
            return

    book = Book(
        title=args.title,
        isbn=args.isbn,
        price=args.price,
        stock=args.stock,
        author=Author(
            name=args.author
        ),
    )

    books.append(book.model_dump())

    save_catalog(books)

    print("Book added successfully.")


def list_books(args):
    books = load_catalog()

    if not books:
        print("No books found.")
        return

    for book in books:
        print(f"Title: {book.get('title')}")
        print(
            f"Author: "
            f"{book.get('author', {}).get('name')}"
        )
        print(f"ISBN: {book.get('isbn')}")
        print(f"Price: {book.get('price')}")
        print(f"Stock: {book.get('stock')}")
        print("-" * 30)


def search_books(args):
    books = load_catalog()

    query = args.query.lower()

    found = False

    for book in books:
        title = book.get("title", "").lower()

        author = book.get(
            "author", {}
        ).get("name", "").lower()

        if query in title or query in author:
            found = True

            print(f"Title: {book.get('title')}")
            print(f"Author: {book.get('author', {}).get('name')}")
            print(f"ISBN: {book.get('isbn')}")
            print(f"Price: {book.get('price')}")
            print(f"Stock: {book.get('stock')}")
            print("-" * 30)

    if not found:
        print("No books found.")


def delete_book(args):
    books = load_catalog()

    new_books = []

    found = False

    for book in books:
        if book.get("isbn") == args.isbn:
            found = True
        else:
            new_books.append(book)

    if not found:
        print("Book not found.")
        return

    save_catalog(new_books)

    print("Book deleted successfully.")


def main():
    parser = argparse.ArgumentParser(
        description="BookVerse CLI"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    add_parser = subparsers.add_parser(
        "add",
        help="Add a new book"
    )

    add_parser.add_argument(
        "--title",
        required=True
    )

    add_parser.add_argument(
        "--author",
        required=True
    )

    add_parser.add_argument(
        "--isbn",
        type=int,
        required=True
    )

    add_parser.add_argument(
        "--price",
        type=float,
        required=True
    )

    add_parser.add_argument(
        "--stock",
        type=int,
        default=1
    )

    add_parser.set_defaults(
        func=add_book
    )

    list_parser = subparsers.add_parser(
        "list",
        help="List all books"
    )

    list_parser.set_defaults(
        func=list_books
    )

    search_parser = subparsers.add_parser(
        "search",
        help="Search books by title or author"
    )

    search_parser.add_argument(
        "query",
        help="Title or author"
    )

    search_parser.set_defaults(
        func=search_books
    )

    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a book"
    )

    delete_parser.add_argument(
        "--isbn",
        type=int,
        required=True
    )

    delete_parser.set_defaults(
        func=delete_book
    )

    args = parser.parse_args()

    try:
        args.func(args)

    except InvalidBookError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()