lst = [1, 2, 3, 4]

# result = []
# for item in lst:
#     result.append(item**2)

# print(result)

# result = [number**2 for number in lst]
# print(result)

def sqr(x):
    return x**2

result = map(sqr, lst)
# print(list(result))




lst = [1, 2, 3, 4, 5, 6, 7, 8]
result = [number for number in lst if number > 5]
result = filter(lambda x: x > 5, lst)
print(list(result))