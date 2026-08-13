from dataclasses import dataclass

@dataclass
class Book():
    title: str
    isbn: int
    author: str
    price: int
    stock: int

    def __str__(self) -> str:
        return f"Title: {self.title} ISBN: {self.isbn} | Author: {self.author} | Price: {self.price} | Stock: {self.stock}"

b1 = Book("ABC", 12, "XYZ", 12, 2)
print(b1)

@dataclass
class Author():
    name: str
    bio: str

    def __repr__(self) -> str:
        return f"Name: {self.name} | Bio: {self.bio}"

a1 = Author("Atharva Phadtare", "I am an author")
print(a1)

@dataclass
class Order():
    books: list[Book]

    def total_price(self) -> int:
        return sum(book.price for book in self.books)

    def total_stock(self) -> int:
        return sum(book.stock for book in self.books)

order = Order([
    Book("1984",123, "George Orwell", 10, 3),
    Book("Dune",456,  "Frank Herbert", 15 , 2),
])

print("Total Price: ", order.total_price())
print("Total Stock: ", order.total_stock())