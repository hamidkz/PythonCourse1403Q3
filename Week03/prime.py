def is_prime(number):
    maq = []
    for i in range(1, number + 1):
        rem = number % i
        if rem == 0:
            maq.append(i)
    return True if len(maq) == 2 else False

for i in range(100, 120):
    print(i, is_prime(i))

# 8 = 2 * 4 = 2 * 2 * 2 = 2 ** 3
# 18 = 3 * 6 = 3 * 3 * 2 = 2 ** 1 * 3 ** 2

