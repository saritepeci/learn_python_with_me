from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass 

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{'Circle': {str(self.calcArea())}}}"

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return (self.side ** 2)

    def toJSON(self):
        return f"{{'Square': {str(self.calcArea())}}}"


#g = GraphicShape()

c = Circle(10)
print(c.calcArea())
print(c.toJSON())


s = Square(4)
print(s.calcArea())
print(s.toJSON())

