def f(x, y, z=None):
    return x + y + z if z is not None else x + y

print(f(1, 5, 2))