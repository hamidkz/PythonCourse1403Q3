lst = [1, 2, 2, 3, 4, 4, 4, 5]
# output: [1, 2, '-', 3, 4, '-', '-', 5]

memory = lst[0]
for i in range(1, len(lst)):
    if lst[i] == memory:
        lst[i] = '-'
    else:
        memory = lst[i]
print(lst)

