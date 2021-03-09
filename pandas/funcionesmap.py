def potenciador(lista):
    listaCuadrados2 = []
    for elemento in lista: 
        valor = elemento **2
        listaCuadrados2.append (valor)
    return listaCuadrados2

lista = [2, 25, 34, 65, 8]
potenciador = lambda valor = 0 : valor **2
print(potenciador(4))
listaCuadrados = list (map(potenciador, lista))
print (listaCuadrados)
listaCuadrados2 = []

lista3 = [2,24,5,45,122,3]
listaCuadrados2 = list(map(potenciador,lista3))
print(listaCuadrados2)

retornarListaCuadrados = lambda listaEntrada = [] : list(map(potenciador, listaEntrada))
lista4 = [2, 34, 5, 76, 59]
listaCuadrados4 = retornarListaCuadrados(lista4)
print(listaCuadrados4)

n= int (input("ingrese valor a restar: "))
restarN = lambda valor : valor - n 
print(restarN(3))
restarNlista = list (map(restarN, lista4))
print (restarNlista)

# normalizar 

mayor = max(lista4)
dividir = lambda valor = 0 : round (valor/mayor,2)
listanormalizada = list(map(dividir,lista4))

print(listanormalizada)

# IMC

pesos = [56,77,85,46,89]
estaturas = [1.65,1.78,1.92,1.49,1.84]

imc = lambda peso = 0 , estatura = 1 : peso / estatura **2 
imclistas = list(map(imc,pesos,estaturas))
print(imclistas)

# Area de un triangulo
bases = [2,34,4,6,234,8]
alturas = [23,49,3,9,48,23]
divisores = [2,2,2,2,2,2]
calcularAreastriangulo = lambda base=0 , altura= 0, divisores=1 : base*altura/divisores
listaAreastriangulo = list(map(calcularAreastriangulo, bases,alturas,divisores))
print(listaAreastriangulo)

print(sum(bases))

# Funciones reduce

from functools import reduce 
sumaElementos = lambda acumulado = 0, elemento=0 : acumulado + elemento
sumar = reduce(sumaElementos, bases)
print(sumar)

multiplicarElementos = lambda acumulado = 0, elemento = 1 : acumulado*elemento
multiplicar= reduce(multiplicarElementos, bases)
print(multiplicar)
print (multiplicar/sumar)