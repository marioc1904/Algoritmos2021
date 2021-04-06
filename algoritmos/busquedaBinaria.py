def busquedaBinaria(lista,encontrar):




    isInlist = False
    lista.sort()
    izq = 0 
    der = len(lista)-1
    while izq <= der and isInlist== False:
        print (lista)
        medio = (izq+der)//2
        print ('calculo medio', (izq+der)//2)
        print (f'valor izquierda {izq}, valor medio {medio}, valor derecha {der}')

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
