# funciones map 
numeroslistas = [1,2,3,4,5]
numeroslistasCuadrado = []

for elemento in numeroslistas:
    numeroslistasCuadrado.append(elemento**2)
print(numeroslistasCuadrado)

cuadrado = lambda base: base**2
listaCuadrados = list(map(cuadrado, numeroslistas))

restarDos = lambda numero: numero -2
listaRestada= list(map(restarDos, numeroslistas))
print (listaCuadrados)
print (listaRestada)