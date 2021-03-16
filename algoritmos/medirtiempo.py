import time
Tiempoinicio = time.time() 
print('Hola a todos')

Tiempofinal = time.time()
delta = Tiempofinal - Tiempoinicio 
print(delta)


for i in range(1000):
    print(i)

print ('hola a todos')
x= 123
for i in range (x):
    print (i)

# instrucciones 
print ('hola a todos')
x = 123
for i in range(x):
    for j in range(x):
        print(i)

# cierre de conteo 
Tiempofinal= time.time()
delta = Tiempofinal - Tiempoinicio
print(delta)
