
class Animal:
    def __init__(self):
        """Constructor for Animal Class"""

    def communicate(self):
        raise NotImplementedError("Abstract method communicate not implemented in this subclass.")

class Bird(Animal):
    def __init__(self):
        Animal.__init__(self)

    def communicate(self):
        print("Chirp chirp, tweet tweet, caw caw")

b = Bird()
b.communicate()

a = Animal()