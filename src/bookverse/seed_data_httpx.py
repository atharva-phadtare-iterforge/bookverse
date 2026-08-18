import asyncio
import httpx
from .schemas.schemas import Book, Author
import json

async def get_books() -> list[Book]:
    async with httpx.AsyncClient() as client:
        params = {
            "q": "api",
            "limit": 20
        }
        response = await client.get("https://openlibrary.org/search.json", params=params)
        response.raise_for_status()
        data = response.json()

        books = []

        for book in data.get("docs", []):
            authors = book.get("author_name", [])
            isbns = book.get("isbn", [])

            mapped_book = Book(
                title=book.get("title", "Unknown"),
                isbn=isbns[0] if isbns else 0,
                price=120,
                stock=1,
                author=Author(
                name=authors[0] if authors else "Unknown"
                ),
            )
            books.append(mapped_book)

    return books


with open('books.json', 'w') as file:
    books = asyncio.run(get_books())
    json.dump(
        [book.model_dump() for book in books],file, indent=4
    )