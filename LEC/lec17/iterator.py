def double(x):
    """print('**',x,'=>',2*x,'**')"""
    return 2*x

"""
filter function
>>>filter(f,m)
f=lambda y:y>=10
m=map(double, range(3,7))
f在前,为过滤函数;m在后;为输入判断值的函数
>>>t=filter(f,m)
>>>next(t)
到5停,但其实没有遍历完整
后面还有一个6

"""

def plus_minus(x):
    yield x
    yield -x

    
def prefixes(s):
    if s:
        yield from prefixes(s[:-1])
        yield s
        
def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
