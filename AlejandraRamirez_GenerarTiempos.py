import numpy as np 
import time

t0 = time.time()

#funcion que retorna el N-esimo termino de la secuencia de fibonacci
#Donde el termino 0 es 0, el termino 1 es 1, el termino 2 es 1 ...
def fibonacci(N):
    #Caso base, se retorna N si es menor o igual a 1
    if N <= 1:
	return N
    #De lo contrario, se ejecuta la operacion siguiente
    else:
	return(fibonacci(N-1) + fibonacci(N-2))

print fibonacci(2)

def get_time()

t1 = time.time()-t0
