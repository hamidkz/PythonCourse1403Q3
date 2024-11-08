# Change for test on github

def f(x):
    z = x+2
    def g(y):
        return y**2    
    return g(z)

print(g(1))