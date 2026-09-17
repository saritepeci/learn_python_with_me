class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    # Use __str__() to return a string representation of the object
    def __str__(self):
        return f"'{self.title}' by {self.author}, costs {self.price:.2f} €"

    # Use __getattribute__() called when an attr is retrieved. Don't directly access
    # the  attribute name otherwise a recursive loop is created.
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    # Use __setattr__() called when an attr is set. Validate the price before setting it.
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("Price must be a float")
        return super().__setattr__(name, value)

    # Use getattr() to retrieve an attribute value safely
    def __getattr__(self, name):
        return name + " is not here!"

b1 = Book("The snow", "Orhan Pamuk", 39.99)
b2 = Book("Martin Eden", "Jack London", 29.99)

print(b1)   
print(b2)

b1.price = float(40) # Update the price of b1 to 40.0
print(b1)