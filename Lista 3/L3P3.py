class Quadrilateral(object):

    def __init__(self):
        self.sides = 4

class RegularPolygon(object):

    def __init__(self, sides=0, color="white"):
        self.sides = sides

class Square(Quadrilateral, RegularPolygon):

    def __init__(self):
        super().__init__()

square = Square()