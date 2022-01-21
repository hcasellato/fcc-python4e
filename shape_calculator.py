class Rectangle():
    def __init__(self, width, height):
        self.width  = width
        self.height = height
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (2*self.width + 2*self.height)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        pic = ""
        if (self.height and self.width) > 50:
            return "Too big for picture."
        for i in range(self.height):
            pic += "*"*self.width + "\n"
            i += 1
        return pic
    def get_amount_inside(self, poly):
        return self.get_area() // poly.get_area()
class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side
    def __str__(self):
        return "Square(side={})".format(self.height)
    def set_side(self, new_side):
        self.height = new_side
        self.width  = new_side
    def set_width(self, new_width):
        self.height = new_width
        self.width  = new_width
    def set_height(self, new_height):
        self.height = new_height
        self.width  = new_height

# Ran 15 tests in 0.001s