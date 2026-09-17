class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # Use __str__() to return a string representation of the object
    def __str__(self):
        return f"'{self.title}' by {self.author}, costs {self.price:.2f} €"

    # Use __repr__() to return a string representation of the object that can be used to recreate the object
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"

    # Use __eq__() to compare two Book objects for equality between 2 objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            return ValueError("Cannot compare Book with non-Book")
        
        return (self.title == value.title and self.author == value.author and self.price == value.price)

    # Use __ge__() establishes => relationship with another object
    def __ge__(self, value):
        if not isinstance(value, Book):
            return ValueError("Cannot compare Book with non-Book")
        return self.price >= value.price

    # Use __gt__() establishes > relationship with another object
    def __gt__(self, value):
        if not isinstance(value, Book):
            return ValueError("Cannot compare Book with non-Book")
        return self.price > value.price

    # Use __le__() establishes <= relationship with another object
    def __le__(self, value):
        if not isinstance(value, Book):
            return ValueError("Cannot compare Book with non-Book")
        return self.price <= value.price

    # Use __lt__() establishes < relationship with another object
    def __lt__(self, value):
        if not isinstance(value, Book):
            return ValueError("Cannot compare Book with non-Book")
        return self.price < value.price

b1 = Book("The snow", "Orhan Pamuk", 20)
b2 = Book("Martin Eden", "Jack London", 15)
b3 = Book("1984", "George Orwell", 18)
b4 = Book("The snow", "Orhan Pamuk", 20)

print(b1 == b4)     # If you don't use __eq__() method, this would be False
print(b1 == b2) 
print(b1 == 458)    # Value Error : Cannot compare Book with non-Book

print(b1 >= b2)    # True if b1's price is greater than or equal to b2's price
print(b1 < b3)     # True if b1's price is less than b3's price


books = [b1, b2, b3, b4]
books.sort()
print([(book.title, book.price) for book in books])
