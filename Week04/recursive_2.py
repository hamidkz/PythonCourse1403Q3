# 4*7 = 7 + 7 + 7 + 7
# 4*7 = 7 + (7 + 7 + 7) = 7 + 3*7 => a*b = b + (a-1)*b 
# 4*7 = 7 + (7 + 7 + 7) = 7 + 7 + 2*7 = 7 + 7 + 7 + 1*7

def mult(a, b):
    return a * b

def mult_2(a,b):
    result = 0
    for i in range(a):
        result += b
    return result

def mult_rec(a, b):
    # if a == 1:
    #     return b
    # else:
    #     return b + mult_rec(a-1, b)
    return b if a == 1 else b + mult_rec(a-1, b)

print(mult(2,3))
print(mult_2(2,3))
print(mult_rec(2,3))