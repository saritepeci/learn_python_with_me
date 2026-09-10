class Vehicle: 
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")         # Same --->>>  Vehicle.__init__(self, "Car")
        self.wheels = 4
        self.doors = 4
        self.engine = enginetype

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Car")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2 
        self.doors = 0
        self.engine = enginetype

car1 = Car("gas")
car2 = Car("electric")
mc1  = Motorcycle("gas", True)

