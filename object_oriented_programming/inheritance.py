class Publication:
    def __init__(self, title, price):
        self.title      = title
        self.price      = price

class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.publisher  = publisher
        self.period     = period

# The super().__init__(title, price) call initializes the attributes inherited from the parent 
# Publication class inside the child Book class.

class Book(Publication):    
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages  = pages

class Magazine(Periodical):    
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)
        # self.title      = title
        # self.publisher  = publisher
        # self.period     = period
        # self.price      = price

class Newspaper(Periodical):    
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, publisher, period)


b1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, 10.99)
m1 = Magazine("National Geographic", "National Geographic Partners", 120, "Monthly")
n1 = Newspaper("The New York Times", "The New York Times Company", 40, "Daily")

print(b1.author)
print(m1.publisher)
print(b1.price, m1.price, n1.price)
