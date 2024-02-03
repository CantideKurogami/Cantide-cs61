def sum_digits(n):
    if n<10:
        return n
    else:
        pre,last=n//10,n%10
        return sum_digits(pre)+last

def fact(n):
    if n==0:
        return 0
    else:
        return n*fact(n-1)
    
"""mutual recursion"""
def luhn_sum(n):
    if n<10:
        return n
    else:
        pre,last=n//10,n%10
        return luhn_sum_double(pre)+last
    
def luhn_sum_double(n):
    pre,last=n//10,n%10
    luhn_digit=sum_digits(2*last)
    if n<10:
        return luhn_digit
    else:
        return luhn_sum(pre)+luhn_digit
    