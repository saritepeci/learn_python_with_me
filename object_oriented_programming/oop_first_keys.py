# Object-Oriented Programming (OOP) - First Keys
class Book:
    def __init__(self, title, author, year, pages, price):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.price = price
        self._secret = "This is a secret attribute"  # private
    # create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discounted(self, amount):
        self._discount = amount

# create instances of the Book class
b1 = Book("The Great Gatsby", "F. Scott Fitzgersald", 1925, 218, 10.99)
b2 = Book("Martin Eden", "Jack London", 1909, 416, 12.99)
b3 = Book("Snow", "Orhan Pamuk", 2002, 400, 14.99)

#print the price of books
print("Price of b1:", b1.get_price())

# get discounted price of books
print("Price of b2:", b2.get_price())
b2.set_discounted(0.25)
print("Discounted price of b2:", b2.get_price())

print(b2._secret)   # accessing private attribute (not recommended)