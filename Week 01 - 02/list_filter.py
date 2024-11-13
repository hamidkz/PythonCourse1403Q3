list = []
for i in range(10):
    if i % 2 == 0:
        list.append(i)

list2 = [number for number in range(10) if number % 2 == 0]

print(list)
print(list2)