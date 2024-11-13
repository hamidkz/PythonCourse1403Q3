lst = [9, -3, 16, -50, 17]

def sqr(x):
    return x**2

sorted_list_1 = sorted(lst, key=sqr)
sorted_list_2 = sorted(lst, key=lambda n: n**2)

print(sorted_list_1)
print(sorted_list_2)
