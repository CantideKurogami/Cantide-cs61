from operator import floordiv , mod

def divide_exact(n,d):
    return floordiv(n,d),mod(n,d)
q,r=floordiv(2024,10),mod(2024,10)
print(q)
print(r)