
class Vehicle:
    def __init__(self, owner):
        self.tire_count = None
        self.has_engine = None
        self.owner = owner

        # skipping getters/setters for now

    def __str__(self):
        return f"owner = {self.owner}, tires = {self.tire_count}, engine = {self.has_engine}"


class Car(Vehicle):
    def __init__(self, owner):
        Vehicle.__init__(self, owner)
        self.tire_count = 4
        self.has_engine = True

    # skipping getters/setters for brevity

    def __str__(self):
        return "Car; " + Vehicle.__str__(self)


class Bicycle(Vehicle):
    def __init__(self, owner):
        Vehicle.__init__(self, owner)
        self.tire_count = 2
        self.has_engine = False

    # skipping getters/setters for brevity

    def __str__(self):
        return "Bicycle; " + Vehicle.__str__(self)

c1 = Car("Philip")
print(c1)
b1 = Bicycle("Colin")
print(b1)
