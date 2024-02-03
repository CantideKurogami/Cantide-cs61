def remove(n,digits):
    exp=0
    kept=0
    while n>0:
        n,last=n//10,n%10
        if last!=digits:
            kept =kept+last*10**exp
            exp+=1
    return kept



def trace1(fn):
    def traced(x):
        print('calling',fn,'on argument',x)
        return fn(x)
    return traced
@trace1
def square(x):
    return x*x

@trace1
def sum_square(n):
    k=1
    total=0
    while k<=n:
        total,k =total+square(k),k+1
    return total