def linedesign():
    print("#"*60)
linedesign()

# funciones lamba 
# lambda entradas: accion 
line = lambda cantidad =12: print('#'*cantidad)
line()
line(2)

sumar = lambda valor1 = 0, valor2 =0 : valor1 + valor2
restar = lambda valor1 = 0, valor2 =0 : valor1 - valor2
multiplicar = lambda valor1 = 0, valor2 =0 : valor1 * valor2
dividir = lambda valor1 = 0, valor2 =0 : valor1 / valor2
resultadosum= sumar(1,2)
print(resultadosum)

calculadora = lambda accion, valor1=0, valor2=0 :print (accion(valor1, valor2))
calculadora (multiplicar,37,33)