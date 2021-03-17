

class Car:
    def __init__(self, owner):
        self.tire_count = 4
        self.has_engine = True
        self.owner = owner

    @property               # property decorator for getters
    def tire_count(self):
        return self._tire_count     # first underscore means "private"

    @tire_count.setter      # decorator for setters
    def tire_count(self, value):
        self._tire_count = value

    @property
    def has_engine(self):
        return self._has_engine

    @has_engine.setter
    def has_engine(self, value):
        self._has_engine = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    def __str__(self):
        return f"Car; owner={self.owner}, tires = {self.tire_count}, engine={self.has_engine}"


c1 = Car("Philip")
print(c1)


class Bicycle:
    def __init__(self, owner):
        self.tire_count = 2
        self.has_engine = False
        self.owner = owner

    # skipping accessors/mutators for brevity
    def __str__(self):
        return f"Bicycle; owner = {self.owner}, tires={self.tire_count}, engine={self.has_engine}"


b1 = Bicycle("John")
print(b1)