def fib(n):
    lst=[0,1]

    for i in range(2,n+1):
        lst.append(lst[-1]+lst[-2])

    return lst

def gn(n):
    x_01=0
    x_02=1
    yield x_01
    yield x_02

    for i in range(2,n+1):
        yield x_01+x_02
        x_01,x_02=x_02,x_01+x_02

x=fib(10)
xf=gn(10)
print(x)
print(list(xf))