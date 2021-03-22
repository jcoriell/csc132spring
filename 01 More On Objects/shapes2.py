class Shape:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
    # getters/setters being skipped for brevity

    def draw(self):
        for _ in range(self.height):
            print("* " * self.width)


class Rectangle(Shape):
    def __init__(self, width, height):
        Shape.__init__(self, width, height)

class Square(Shape):
    def __init__(self, width):
        Shape.__init__(self, width, width)

class Triangle(Shape):
    def __init__(self, width):
        Shape.__init__(self, width, width)

    def draw(self):
        for i in range(self.width):
            print("* " * (self.width - i))

# create the shapes
r = Rectangle(5, 3)
s = Square(4)
t = Triangle(5)

# draw the shapes
r.draw()
print()
s.draw()
print()
t.draw()