from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Price: {self.price}"

# Create some instances
b1 = Book("The snow", "Orhan Pamuk", 450, 39.99)
b2 = Book("Martin Eden", "Jack London", 352, 29.99)
b3 = Book("1984", "George Orwell", 249, 18.99)

# Access fields
print(b1.title)
print(b1.author)

print(b1)

#__eq__ method is automatically provided by dataclass
print(b1==b2)

# change  book name vs accessing book info
b1.title = "The Snow Updated"
print(b1.bookinfo())

