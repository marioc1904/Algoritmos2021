# funciones filter 
lista = [2,3,4,54,33,8,35,98]
listaPares= []

for elemento in lista: 
    if elemento % 2 == 0:
        listaPares.append(elemento)
print(listaPares)

# con filter 

par = lambda valor: valor % 2 == 0 
listaParesFiltrada= list (filter(par,lista))
print(listaParesFiltrada)

mayores = lambda valor: valor >= 12
listaMayores = list(filter(mayores, lista))
print (listaMayores)