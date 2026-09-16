class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "class A"

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "class B"


class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)    # output: class A because python find a first class (class C(A, B):) 
                            # If you changed you make class C(B, A): -->> class B

c = C()
print(C.__mro__)    #(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
c.showprops()
