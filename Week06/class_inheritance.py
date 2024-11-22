class Shape:
    def surface(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def surface(self):
        return self.width * self.height
       

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def surface(self):
        return self.r ** 2 * 3.14
        

# Interihance ارث بری

rect_1 = Rectangle(3,4)
print(rect_1.surface())

circle_1 = Circle(2)
print(circle_1.surface())

# override overwrite

class MyString(str):
    def capitalize(self):
        return 'NEW CAPITALIZE'

my_string = MyString()
print(my_string.capitalize())
