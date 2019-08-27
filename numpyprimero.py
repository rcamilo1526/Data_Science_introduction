# -*- coding: utf-8 -*-

import numpy as np
#crear arreglo 9x9x9
m1 = np.arange(729).reshape(9,9,9)

#recorrer cada 3 para crear los 27 arreglos de 3x3x3
m2=[]
for i in range (0,7,3):
    for j in range(0,7,3):
        for k in range(0,7,3):
            m2.append(m1[i:i+3,j:j+3,k:k+3])
#funcion de cambio de orden con un swap               
def cambiar_orden(a,b):
    m2[a],m2[b] = m2[b],m2[a]
    return m2

a=int(input('Inserte posición:  '))
b=int(input('Inserte posición a intercambiar:  '))

M= cambiar_orden(a,b)
    
print(M)




