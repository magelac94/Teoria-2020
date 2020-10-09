def corteVarilla(precio,n):
    valores = [ 0 for i in range(n+1)]              #Llenamos de valores 0 una lista de tamaño n+1.
    valores[0] = 0                                  #Ponemos 0 en el primer lugar
    output = list()                                 #Creamos lista de razonamiento, no sirve a efectos del resultado
    lista = [ 0 for i in range(n)]
    for i in range(1,n+1):
        max_val = 0
        for j in range (i):
            valor_actual = precio[j] + valores[i-j-1]
            if(valor_actual>max_val):
                if(i==1):
                    lista[i-1] = j
                    output.append(j)
                else:
                    if((i-j-2)>=0):
                        output.append((j,i-j-2))
                        lista[i-1] = (j,lista[i-j-2])
                    else:
                        output.append(j)
                        lista[i-1] = j
                max_val = valor_actual
        valores[i] = max_val
            
    return (valores,lista)

precio = [2,3,7,100,2,4,5,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,5,4,12,45,54,152,54,185,5212121,21,54,5774,51,21,21,51,54,21,21,54,54,87,12,18,19,1,5]
n=45
tupla = corteVarilla(precio,n)

for i in range(1,len(tupla[0])):
    print("Para varilla de: " + str(i) + " metros, su mejor precio sería: " + str(tupla[0][i]) + " cortada de la forma: " + str(tupla[1][i-1]))