from math import pi,sqrt
from operator import mul

def area(r,shape_const):
    assert r>0, 'a length must be positive'
    return r*r*shape_const
def area_square(r):
    return area(r,1)
def area_circle(r):
    return area(r,pi)
def area_hexagon(r):
    return area(r,3*sqrt(3)/2)

def sum_naturals(n):
    total,k=0,1
    while k<=n:
        total,k=total+k,k+1
    return total

def cube(n):
    return pow(n,3)
def equal(n):
    return n
def pi_term(n):
    return 8/mul((4*n-3),(4*n-1))

def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total

"""
>>>add_three=make_adder(3)
>>>add_three(4)
7
"""
def make_adder(n):
    def adder(k):
        return k+n
    return adder



def search(f):
    x=0
    while not f(x):
        x=x+1
    return x
def square(x):
    return x*x
def inverse(f):
    return lambda y:search(lambda x:f(x)==y)

def positive(x):
    return max(0,square(x)-100)

def if_(c,t,f):
    if c:
        return t
    else:
        return f
def real_sqrt(x):
    
    return if_(x>0,sqrt(x),0.0)

def reasonable(n):
    return n==0 or 1/n!=0
"""与下面这个函数是一样的"""
x=0
abs(1/x if x!=0 else 0)