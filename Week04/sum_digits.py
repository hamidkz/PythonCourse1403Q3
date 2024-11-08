num = 456145614561 # -> 16 -> 7
# output: 7

def sum_digits(num):
    return sum([int(d) for d in str(num)]) # [4, 5, 6, 1]


while num > 10:
    num = sum_digits(num)

print(num)