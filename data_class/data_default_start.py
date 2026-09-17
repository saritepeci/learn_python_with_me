from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20, 50))


@dataclass
class Book:
    title: str = "No Title"
    author: str = "Unknown Author"
    pages: int = 0
    price: float = field(default_factory = price_func)

    def __post_init__(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Price: {self.price}")

# Create some instances
b1 = Book()
b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b3 = Book("1984", "George Orwell", 249)

# Access fields

print(b1)
print(b2)
print(b3)
