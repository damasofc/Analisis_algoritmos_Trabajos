import sys
import timeit

x = int(sys.argv[1])
y = int(sys.argv[2])

def ordenar(articles):
    for i in articles:
        i.append(i[0]/i[1])
    
    n = len(articles)
    for i in range(1,n):
        for j in range(n-i):
            if articles[j][2] < articles[j+1][2]:
                articles[j],articles[j+1] = articles[j+1],articles[j]
    return articles


def maxArticles(n,tam,articles):
    articles = ordenar(articles)
    peso = 0
    valRes = 0
    for i in range(0,n):
        if peso == tam:
            break
        if peso + articles[i][1] <= tam:
            peso += articles[i][1]
            valRes += articles[i][0]
        else:
            valRes += ((tam-peso)/articles[i][1])* articles[i][0]
            peso += tam - peso

    return valRes

articles = []
print("Ingrese datos: ")
for i in range(0,x):
    datos = input(str(i+1)+". ")
    valores = datos.split(" ")
    articles.append([int(valores[0]),int(valores[1])])

start = timeit.default_timer()
m = maxArticles(x,y,articles)
stop = timeit.default_timer()
print(m)
print("\nTime elapse: ", stop-start)