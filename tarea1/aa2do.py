import sys
import timeit

x = int(sys.argv[1])
y = int(sys.argv[2])


def maxArticles(n,tam,articles):
    for k,v in articles.items():
        print(k," - ",v)

articles = {}
print("Ingrese datos: ")
for i in range(0,x):
    datos = input("1. ")
    valores = datos.split(" ")
    articles[valores[0]] = valores[1]

start = timeit.default_timer()
m = maxArticles(x,y,articles)
stop = timeit.default_timer()
print(m)
print("\nTime elapse: ", stop-start)