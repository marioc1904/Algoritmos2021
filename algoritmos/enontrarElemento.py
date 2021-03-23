listaNombres = ['Karla','Arturo','Laura','Juan']
print ('Karla' in listaNombres)

encontro = False
busqueda = 'Karla'
for elemento in listaNombres:
    if elemento == busqueda:
        encontro = True

print(encontro)
print (listaNombres.index('Karla'))

for i in range (len(listaNombres)):
    if listaNombres[i]== busqueda:
        posicion = i
print(posicion)