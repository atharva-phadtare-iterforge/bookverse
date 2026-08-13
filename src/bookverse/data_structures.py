books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "price": 29, "stock": 10},
    {"title": "1984", "author": "George Orwell", "price": 19, "stock": 15},
    {"title": "Atomic Habits", "author": "James Clear", "price": 49, "stock": 8},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 24, "stock": 5},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 10, "stock": 7},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 12, "stock": 12},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "price": 5, "stock": 9},
    {"title": "Harry Potter", "author": "J.K. Rowling", "price": 11, "stock": 20},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "price": 35, "stock": 6},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "price": 29, "stock": 11}
]


def print_report(*args, **kwargs):
    for book in args:
        print(
            f"Title: {book['title']} | "
            f"Author: {book['author']} | "
            f"Price: ${book['price']} | "
            f"Stock: {book['stock']}"
        )

    print("\nReport:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


sortedbooks = sorted(books, key=lambda book: book["title"], reverse=True)

newbooks = [book for book in sortedbooks if book["price"] < 20]

print_report(*newbooks, category="Books under $20", total=len(newbooks))