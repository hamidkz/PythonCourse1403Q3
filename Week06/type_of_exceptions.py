# NameError
# print(a)

# TypeError
# t = 'hamid' + 3

# ValueError
# int('hamid')

# IndexError
# list = [1,2,3]
# print(list[10])

# KeyError
# dictionary = {
#     'name': 'hamid'
# }

# print(dictionary['age'])

# ModuleNotFoundError
# import j_datetime

# AttributeError
# t = 'hamid'.Lower()


# a = 10
# a = 20
# a = 30
# print(a)

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

result = fact(3)
print(result)