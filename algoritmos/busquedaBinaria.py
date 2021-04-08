def busquedaBinaria(lista,encontrar):




    isInlist = False
    lista.sort()
    izq = 0 
    der = len(lista)-1
    while izq <= der and isInlist== False:
        medio = (izq+der)//2

        if lista [medio] == encontrar:
            isInlist = True 
        elif lista [medio] > encontrar:
            der = medio + 1 
        else: 
            izq = medio + 1
    return isInlist



listaEntrada = [2,12,34,5,11,59,4,3,1]
valorEncontrar = int(input('ingrese un numero: '))
print (busquedaBinaria(listaEntrada,valorEncontrar))
