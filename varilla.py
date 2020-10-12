def agregarCeros(precios,n):
    for i in range(len(precios),n):
        precios.append(0)
    return precios
def corteVarilla(precio,n):
    if(n>len(precio)):
        agregarCeros(precio,n)
    valores = [ 0 for i in range(n+1)]              #Llenamos de valores 0 una lista de tamaño n+1.
    valores[0] = 0                                  #Ponemos 0 en el primer lugar
    lista = [ 0 for i in range(n)]
    for i in range(1,n+1):
        max_val = 0
        for j in range (i):
            valor_actual = precio[j] + valores[i-j-1]
            if(valor_actual>max_val):
                if(i==1):
                    lista[i-1] = j
                else:
                    if((i-j-2)>=0):
                        lista[i-1] = (j,lista[i-j-2])
                    else:
                        lista[i-1] = j
                max_val = valor_actual
        valores[i] = max_val
            
    return (valores,lista)

precio = [2,3,7,100,2,4]
n=3
tupla = corteVarilla(precio,n)

for i in range(1,len(tupla[0])):
    print(str(i) +": Para varilla de: " + str(i) + " metros, su mejor precio sería: " + str(tupla[0][i]) + " cortada de la forma: " + str(tupla[1][i-1]))