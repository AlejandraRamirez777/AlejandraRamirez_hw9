import numpy as np 
import time

#funcion que retorna el N-esimo termino de la secuencia de fibonacci
#Donde el termino 0 es 0, el termino 1 es 1, el termino 2 es 1 ...

def fibonacci(N):
    #Caso base, se retorna N si es menor o igual a 1
    if N <= 1:
	return N
    #De lo contrario, se ejecuta la operacion siguiente
    else:
	return(fibonacci(N-1) + fibonacci(N-2))

#print fibonacci(2)

#funcion que retorna tiempo que tarda fibonacci para el N-esimo termino
def get_time(N):
    t0 = time.time()
    fibonacci(N)
    t1 = time.time()-t0
    return t1

#ciclo para imprimir primeros 35 valores de N con el tiempo se tarda

for i in range(35):
   print str(i) + "," + str(get_time(i))
