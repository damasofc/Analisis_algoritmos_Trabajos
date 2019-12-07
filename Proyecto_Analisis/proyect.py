import sys
import timeit

num = int(sys.argv[1])


def getGood(t,good,bad,idConsults):
    #evaluar
    res = ""
    for i in range(0,len(idConsults)):
        if (good[idConsults[i]] - bad[idConsults[i]]) >= t:
            res = res + "1 "
        else:
            res = res + "0 "
            

    
    return res

t = int(input());
good = {}
bad = {}
for i in range(0,num):
    datos = input()
    valores = datos.split(" ")
    good[int(valores[0])] = int(valores[1])
for i in range(0,num):
    datos = input()
    valores = datos.split(" ")
    bad[int(valores[0])] = int(valores[1])
nConsults = int(input());
c = input();
idConsults = c.split(" ")
for i in range(0,len(idConsults)):
    idConsults[i] = int(idConsults[i])




start = timeit.default_timer()
m = getGood(t,good,bad,idConsults)
stop = timeit.default_timer()
print(m)
print("\nTime elapse: ", stop-start)