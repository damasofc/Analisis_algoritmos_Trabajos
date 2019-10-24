import sys
import timeit
x = int(sys.argv[1])


def minMonedas(a):
    falta = a
    cantMonedas = 0
    while falta != 0:
        if falta - 10 >= 0:
            cantMonedas += 1
            falta -= 10
        elif falta - 5 >= 0:
            cantMonedas += 1
            falta -= 5
        else:
            cantMonedas += 1
            falta -= 1
    return cantMonedas

start = timeit.default_timer()
m = minMonedas(x)
stop = timeit.default_timer()
print(m)
print("\nTime elapse: ", stop-start)