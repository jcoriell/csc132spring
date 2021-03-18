
class Vehicle:
    def __init__(self, owner):
        self.tire_count = None
        self.has_engine = None
        self.owner = owner

    # skipping getters/setters

    def __str__(self):
        return f"owner = {self.owner}, tire count = {self.tire_count}, engine = {self.has_engine}"

class Car(Vehicle):
    def __init__(self, owner):
        Vehicle.__init__(self, owner)
        self.tire_count = 4
        self.has_engine = True

    def __str__(self):
        return "Car; " + Vehicle.__str__(self)


class Cycle(Vehicle):
    def __init__(self, owner):
        Vehicle.__init__(self, owner)
        self.tire_count = 2

    def __str__(self):
        return Vehicle.__str__(self)

class Bicycle(Cycle):
    def __init__(self, owner):
        Cycle.__init__(self, owner)
        self.has_engine = False

    def __str__(self):
        return "Bicycle; " + Cycle.__str__(self)

class Motorcycle(Cycle):
    def __init__(self, owner):
        Cycle.__init__(self, owner)
        self.has_engine = True

    def __str__(self):
        return "Motorcycle; " + Cycle.__str__(self)

c1 = Car("Claire")
bike = Bicycle("Grant")
moto = Motorcycle("Ashli")

print(c1)
print(bike)
print(moto)

