# Object Oriented Programming برنامه نویسی شیئ گرا
# OOP

# Class -> object | instance
# Machine -> Dishwasher, Pride

# class Car:
#     pass

# my_car = Car()

# print(type(my_car))

# method: Car: drive(), boogh(), start()
# property: Car: color, size


class Car:
    def __init__(self, name):
        self.name = name

my_car_1 = Car('Pride')
my_car_2 = Car('Jack S5')
print(my_car_1.name)
print(my_car_2.name)

# class Circle:
#     def __init__(self, r):
#         self.r = r

# my_circle = Circle(4)
