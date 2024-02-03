from math import gcd
def rational(n,d):
    g=gcd(n,d)  
    return [n//g,d//g]

"""abstraction barrier"""


