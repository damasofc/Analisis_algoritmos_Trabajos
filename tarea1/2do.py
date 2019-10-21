import sys
import timeit
x = int(sys.argv[1])
y = int(sys.argv[2])


def mcm(a,b):
    bigger = a if(a > b) else b
    lesser = b if(a > b) else a
    i = 1
    while True:
        if (bigger*i % lesser) == 0:
            return bigger*i
        i += 1

start = timeit.default_timer()
m = mcm(x,y)
stop = timeit.default_timer()
print(m)
print("\nTime elapse: ", stop-start)