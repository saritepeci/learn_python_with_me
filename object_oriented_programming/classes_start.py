class Book: 
    # Properties defined at the class level are shared by all instances of the class
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # double-underscore properties are hidden from other classes
    __booklist = None
    
    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

    # Instance method recieve a specific object instance as an argument and operate on data specific to that instance
    def self_title(self, newtitle):
        self.title = newtitle

    # Create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # Create a static method 
    #You can added @staticmethod in this methode
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def __str__(self):
        return f"{self.title} ({self.booktype})"


# Access the class attribute
print("Book types: ", Book.get_book_types())


# Create some book instances
b1 = Book("Title1", "HARDCOVER")
b2 = Book("Title1", "PAPERBACK")

# Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)

#print(thebooks)

for book in thebooks:
    print(book)