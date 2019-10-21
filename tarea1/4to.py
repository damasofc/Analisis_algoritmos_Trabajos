import sys
import timeit
x = int(sys.argv[1])


def fibo(val):
    arrRes = []
    arrRes.append(0)
    arrRes.append(1)
    if val >= 2:
        for i in range(2,val+1):
            arrRes.append(arrRes[i-1] + arrRes[i-2])
    return arrRes[val]
def sumFib(a):
    if a == 0 or a == 1 or a == 2:
        return a
    else:
        return (sumFib(a-1)+fibo(a))%10

start = timeit.default_timer()
m = sumFib(x)
stop = timeit.default_timer()
print(m)
print("\nTime elapse: ", stop-start)