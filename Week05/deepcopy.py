import copy

a = [
    [1,2],
    [3,4]
]

b = copy.deepcopy(a)
b[0][0] = 100

print(a)
print(b)
