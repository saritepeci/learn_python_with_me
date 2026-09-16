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

b1 = Book("The snow", "Orhan Pamuk", 20)
b2 = Book("Martin Eden", "Jack London", 15)

print(b1)   
print(b2)

