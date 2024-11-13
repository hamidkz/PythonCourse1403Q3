import random

list = []
for i in range(1000000):
    rnd = random.random()
    list.append(rnd)

avg = sum(list) / len(list)
print(avg)
