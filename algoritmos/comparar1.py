import time 
import ordenamiento_burbuja as ob
import ordenamiento_insercion as oi
import random as r 

lista = []
for i in range(1200):
    lista.append(r.randint(1,10000))
listaCopia = lista.copy()

# inicio 
inicio = time.time()

# instrucciones
ob.ordenamientoBurbuja(lista)

oi.ordenamientoInsercion(lista)
# delta 
deltaOb = time.time() - inicio

deltaOi = time.time() - inicio


# inicio 
inicio = time.time()

# instrucciones

listaCopia.sort()
# delta 

deltaSort = time.time() - inicio 
print(deltaSort)
print (deltaOb)
print (deltaOi)
print(deltaSort >= deltaOb)
print(deltaSort >= deltaOi)