
p = [2, 3, 7, 9,10,11,12]
precios=[]
j=0
def varillaRecursiva(n,precios,j):
    if n <= 1:
        return n
    costo = -1
    for i in range(1, n+1):
        costo = max(costo, (p[i-1]+ varillaRecursiva(n-i,precios,j))) 
        print(costo)
    precios.append(costo)
    return costo

print (varillaRecursiva(7,precios,j))
print(precios)

precio = [2,3,7]
n=4
valores = [0 for i in range(n+1)]