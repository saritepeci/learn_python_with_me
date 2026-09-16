class Book:    
    def __init__(self, title, price, author =None):
        self.title = title
        self.price = price
        self.author = author

        # self.authorfname = authorfname
        # self.authorlname = authorlname

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)
        #self.chapters.append((name,pages))
    
    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # Determines what is returned when the object is directly converted to text
    # If you do not use ->>> output ->>>  <__main__.Author object at 0x7f9b8c123450>
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

auth = Author("Leo", "Tolstoy")
b1 = Book("test", 33.33, auth)

b1.addchapter(Chapter("ch1", 122))
b1.addchapter(Chapter("ch2", 92))

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())