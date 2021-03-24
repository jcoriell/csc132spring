
class Plant:
    def __init__(self):
        """Constructor for Plant"""

    def __str__(self):
        return "This is a plant"

class Item:
    def __init__(self):
        """Constructor for Item"""

    def __str__(self):
        return "This is an item"


class Fruit(Plant):
    def __init__(self):
        Plant.__init__(self)
        #super().__init__() another way to call the constructor

    def __str__(self):
        return "This is a fruit"

class SaleItem(Item):
    def __init__(self):
        Item.__init__(self)

    def __str__(self):
        return "This is a SaleItem."

class Banana(SaleItem, Fruit):
    def __init__(self):
        Fruit.__init__(self)
        SaleItem.__init__(self)

    #def __str__(self):
    #    return "This is a banana."

b = Banana()

print(b)