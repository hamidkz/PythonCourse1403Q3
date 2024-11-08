# 1+2+3+...+n = sigma(x)
# 6! = 6 * 5 * 4 * 1

def fact(x):
    r = 1
    for i in range(1, x+1):
        r = r * i
    return r


def f(x):
    return pow(-1, x)/fact(x)

result = 0
for i in range(1, 100000):
    result += f(i)
    print(i, result)

