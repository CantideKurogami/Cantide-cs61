from math import pi,sqrt

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
def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total

a=1 
def fun():
    global a
    print(a)
    a=2