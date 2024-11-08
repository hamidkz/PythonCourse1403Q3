# no_2 = 1
# no_3 = 2
# 18 / 2 = 9 / 3 = 3 /3 = 1
# [[2, 1], [3, 2]]


def is_prime(number):
    maq = []
    for i in range(1, number + 1):
        rem = number % i
        if rem == 0:
            maq.append(i)
    return True if len(maq) == 2 else False

def prime_numbers_less_than(num):
    result = []
    for i in range(2, num):
        if is_prime(i) is True:
            result.append(i)
    return result

num = 4
result = []
for prime in prime_numbers_less_than(num): # 2, 3
    # prime: 2
    no = 0
    while num % prime == 0:
        num = num / prime
        no += 1
    if no > 0: # no: 2
        result.append(
            [prime, no] # [2, 2]
        )        
print(result)