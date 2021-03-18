

class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    # getters/setters being skipped for brevity

    def draw(self):
        for _ in range(self.height):        # underscore is frequently used to indicate
            print("* " * self.width)        # we aren't using the variable within the for loop

r = Rectangle(5, 3)
r.draw()
print()

r2 = Rectangle()
r2.draw()

