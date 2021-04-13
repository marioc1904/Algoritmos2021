# 1, 1/2, 1/4, 1/8, 1/16 ...
#numero 1 -----> 1 (1/2**0) 
#numero 2 -----> 1/2 (1/2**1) 
#numero 3 -----> 1/4 (1/2**2) 
#numero 4 -----> 1/8 (1/2**3) 
#numero 5 -----> 1/16 (1/2**4) 

n = int(input ('ingrese un numero : '))
print(n)


def sucesion(n): 
    return ((1/2)**(n-1))
print (sucesion(n))



# 3, 5, 7, 9, 11
# numero 1 ------> 3 (2*0)+3
# numero 2 ------> 5 (2*1)+3
# numero 3 ------> 7 (2*2)+3
# numero 4 ------> 9 (2*3)+3
# numero 5 ------> 11 (2*4)+3

def sucesion2(n):
    return (2*(n-1))+ 3
print (sucesion2(n))