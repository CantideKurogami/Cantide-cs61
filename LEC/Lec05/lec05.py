from operator import mul
def square(x):
    return x*x

def triple(x):
    return 3*x

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

def curry2(f):
    def h(x):
        def g(y):
            return f(x,y)
        return g
    return h
"""与下列lambda形式相同"""
wtf=lambda f:lambda x:lambda y:f(x,y)
chengyi=wtf(mul)
