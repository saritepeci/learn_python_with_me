ratings=[2,5,9,9,9,10,6,5,3]

ratings_sorted = sorted(ratings)  # Returns a new sorted list
print(ratings)                # Output: [2, 5, 9, 9, 9, 10, 6, 5, 3] 
print(ratings_sorted)         # Output: [2, 3, 5, 5, 6, 9, 9, 9, 10]


reverse_ratings = reversed(ratings)  # Returns an iterator that yields the ratings in reverse order
print(ratings)                # Output: [2, 5, 9, 9, 9, 10, 6, 5, 3] 
print(list(reverse_ratings))  # Output: [3, 5, 6, 10, 9, 9, 9, 5, 2]



class class_circle: # Its same class class_circle(): and class_circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color  = color
    def add_radius(self, r):
        self.radius += r
        return (self.radius)
    def draw_circle(self):
        print(f"Drawing a {self.color} circle with radius {self.radius}")


circle1 = class_circle(5, "red")
print(circle1.radius)  # Output: 5

circle1.add_radius(3)
print(circle1.radius)  # Output: 8

print(circle1.color)   # Output: "red"
circle1.draw_circle()  # Output: Drawing a red circle with radius 8


class class_rectangle:
    def __init__(self, height, width, color):
        self.height = height
        self.width  = width
        self.color  = color
    def area(self):
        return self.height * self.width

rectangle1 = class_rectangle(4, 14, "fuscia")
print(rectangle1.height)  # Output: 4
print(rectangle1.width)   # Output: 14
print(rectangle1.color)   # Output: "fuscia"
print(rectangle1.area())    # Output: 56


