# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:26:45 2019

@author: Estudiantes
"""
from random import randrange
r=randrange(100)
print(r)
tries=0

for i in range(11):
    print('Intento {}:'.format(tries+1))
    a=int(input('Ingrese el numero:  '))
    if a==r:
        print('Adivino el numero {} en {} intentos'.format(a,tries+1))
        break
    elif a>r:
        print('el numero a adivinar es menor\n')
        tries +=1
    elif a<r:
        print('el numero a adivinar es mayor\n')
        tries += 1
else:
    print('\nNo adivino el numero, el numero era {}'.format(r))
        
        
