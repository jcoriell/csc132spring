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

r = Rectangle(5, 3)
s = Square(4)
r.draw()
print()
s.draw()