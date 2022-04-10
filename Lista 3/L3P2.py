def decorator(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper

class RegularPolygon(object):

    def __init__(self, sides=0, color="white"):
        self.sides = sides
        self.color = color
    
    @decorator
    def print_format(self):
        return "I am a polygon of " + str(self.sides) + " sides and my color is " + self.color + "!"

polygon = RegularPolygon(5, "red")
print(polygon.print_format())