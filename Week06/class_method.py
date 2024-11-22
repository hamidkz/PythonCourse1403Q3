class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def surface(self):
        return self.width * self.height

# def mult(w, h):
#     return w * h

# mult(3,4)

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(6, 4)

print('rect_1: ', rect_1.surface())
print('rect_2: ', rect_2.surface())


