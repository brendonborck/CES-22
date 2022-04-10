#from abc import staticmethod, abstractclassmethod

class RegularPolygon(object):

    def __init__(self, sides=0, color="white"):
        self.sides = sides
        self.color = color

    def print_polygon(self):
        print("I am a polygon of " + self.sides + " sides and my color is "  + self.color)

    def change_color(self, color):
        self.color = color
        print("Now I have the color " + color)

    #@abstractmethod
    def print_sides(self):
        pass

    @classmethod
    def from_string(cls, polygon_as_string):
        sides, color = polygon_as_string.split('-')
        polygon_example = cls(sides,color)
        return polygon_example

    @staticmethod
    def is_polygon_valid(sides, angle):
        if angle == (180*(sides-2)/sides):
            print("This polygon is valid!")
            return True
        print("This polygon is NOT valid!")
        return False


class Triangle(RegularPolygon):

    def print_sides(self):
        print("Eu tenho 3 lados")


class Quadrilateral(RegularPolygon):

    def print_sides(self):
        print("Eu tenho 4 lados")


class Pentagon(RegularPolygon):

    def print_sides(self):
        print("Eu tenho 5 lados")



triangle = Triangle(3, "blue")
triangle.print_sides()

quadrilateral = Quadrilateral(4, "blue")
quadrilateral.print_sides()

pentagon = Pentagon(5, "blue")
pentagon.print_sides()

pentagon = Pentagon()
pentagon.change_color("red")

polygon_example = RegularPolygon.from_string('5-orange')

polygon_example.print_polygon()

is_polygon = RegularPolygon.is_polygon_valid(4, 90)
is_polygon = RegularPolygon.is_polygon_valid(4, 100)
