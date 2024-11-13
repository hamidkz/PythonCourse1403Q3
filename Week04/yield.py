# def get_numbers():
#     result = []
#     for i in range(10):
#         result.append(i)
#     return result

# l = get_numbers()
# print(l)

def get_next_number():
    yield 1
    yield 2
    # yield 3
    # yield 4

l = get_next_number()
print('first call: ', next(l))
print('second call: ', next(l))
print('3th call: ', next(l))

# print('first call: ', get_next_number())
# print('second call: ', get_next_number())
# print('3th call: ', get_next_number())
