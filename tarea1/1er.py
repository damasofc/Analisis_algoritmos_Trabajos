import sys
import timeit
x = int(sys.argv[1])


def lastFibN(a):
    m = 0
    b = 1
    if a == 0:
        return 0
    c = 1
    for i in range(2,a+1):
        c = m%10+b%10
        m,b = b, c
    return c

start = timeit.default_timer()
m = lastFibN(x)
stop = timeit.default_timer()
print(m)
print("\nTime elapse: ", stop-start)