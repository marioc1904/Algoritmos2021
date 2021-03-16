# fibonacci 0,1,1,2,3,5,8,13,21,

#---pregunta---#
Pregunta_numero = 'ingrese un número entero :'

#---mensaje error---#
Error_entrada = 'entrada no valida'
#---entradas---#
numero = None
while(numero==None):

    try: 
        numero = int(input(Pregunta_numero))
    except ValueError:
        print (Error_entrada)
print(numero)

numeroAnterior = 0
numeroActual = 1
if (numero ==1):
    print(numeroAnterior)
elif (numero == 2):
    print(numeroActual)
else: 
    for i in range (2, numero+1):
        print(i)
        aux = numeroActual
        numeroActual= numeroAnterior + numeroActual
        numeroAnterior = aux
        print (numeroActual)
    print('salida', numeroActual)