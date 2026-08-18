import requests
from .schemas.schemas import Book, Author
import json


def get_books() -> list[Book]:
    params = {
        "q": "python",
        "limit": 20,
    }

    response = requests.get("https://openlibrary.org/search.json", params=params)
    response.raise_for_status()

    data = response.json()

    books = []

    for id, book in enumerate(data.get("docs", [])):
        authors = book.get("author_name", [])
        isbns = book.get("isbn", [])

        mapped_book = Book(
            id=id,
            title=book.get("title", "Unknown"),
            isbn=isbns[0] if isbns else 12345678,
            price=120,
            stock=1,
            author=Author(
                name=authors[0] if authors else "Unknown"
            ),
        )

        books.append(mapped_book)

    return books





with open('books.json', 'w') as file:
    books = get_books()
    json.dump([book.model_dump() for book in books],file,indent=4)