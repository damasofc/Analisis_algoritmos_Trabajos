import sys
import timeit
x = int(sys.argv[1])
y = int(sys.argv[2])


def pisanoPeriod(m):
    a = 0
    b = 1
    c = a+b
    for i in range(0,m*m):
        c = (a+b)%m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1

def fibo(val):
    arrRes = []
    arrRes.append(0)
    arrRes.append(1)
    if val >= 2:
        for i in range(2,val+1):
            arrRes.append(arrRes[i-1] + arrRes[i-2])
    return arrRes[val]
def modFib(a,b):
    l = pisanoPeriod(b)
    fget = a % l
    return fibo(fget)%b

start = timeit.default_timer()
m = modFib(x,y)
stop = timeit.default_timer()
print(m)
print("\nTime elapse: ", stop-start)