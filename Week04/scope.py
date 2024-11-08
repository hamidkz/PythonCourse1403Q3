a = 200
def my_function():
    global a
    a = 100
    print('a in the function: ', a)

my_function()
print('a out of the function: ', a)