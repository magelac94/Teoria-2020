matriz = list()
resultante = list()
#n <- Cantidad de elementos a elegir
#c <- Capacidad de la mochila
def bag(n,c,data):
    if(len(data)==0):
        return None
    for x in range(n):
        matriz.append([])
        for y in range(c+1):
            matriz[x].append(0)
    for i in range(n):
        for w in range(c+1):
            if data[i][1] <= w:
                matriz[i][w] = max(matriz[i-1][w],data[i][0]+matriz[i-1][w-data[i][1]])           
            else:
                matriz[i][w] = matriz[i-1][w]
    return matriz[n-1][c]

data = [(1,30,"Cartuchera"),(2,5,"Coso1"),(5,6,"Coso2")]
n=3
c=30
print(bag(n,c,data))
print(resultante)

