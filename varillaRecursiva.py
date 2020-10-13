#Pre: que venga ordenado de mayor a menor
priceSize = [(4,5),(3,5),(2,4),(1,1)]
clientOrder = 4
 
def corteVarillaRecursivo(priceSize,clientOrder):
    result = list()
    for position in range(len(priceSize)):
        order = clientOrder
        resultSize = list()
        cutControl(priceSize,order,position,resultSize)
        result.append(resultSize)
    return result

def cutControl(priceSize,order,position,resultSize):
    
    if(position<=len(priceSize)-1):
        
        (size,price) = priceSize[position]
        if(size>order):
            cutControl(priceSize,order,position+1,resultSize)
        else:
            order=order-size
            resultSize.append((size,price))
            if(order!=0):
                cutControl(priceSize,order,0,resultSize)
            else:
                cutControl(priceSize,order,position+1,resultSize)

    else:
        return
        
    
respuestas = corteVarillaRecursivo(priceSize,clientOrder)

if((len(respuestas))>0):
    for respuesta in respuestas:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("option")
        print("====")
        for (size,price) in respuesta:
            
            print("-")
            print("tamano: ")
            print(size)
            print("precio: ")
            print(price)