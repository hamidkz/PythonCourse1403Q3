
# 3! = 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1 = 4 * 3! = 4 * 3 * 2! = 4 * 3 * 2 * 1! = 4 * 3 * 2 * 1

# n! = n * (n-1)!  

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))

n = 3
fact(3) = 3 * fact(2)
fact(2) = 2 * fact(1)
fact(1) = 1