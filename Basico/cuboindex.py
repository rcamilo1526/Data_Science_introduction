# -*- coding: utf-8 -*-
import numpy as np
import copy

cubo = np.arange(729).reshape(9,9,9)
cuboaux = copy.deepcopy(cubo)
  
def cambiarcubo(id1,id2):
    global cuboaux
    #extrayendo los cubos 
    print('El cubo con el indice {}\n'.format(id1))
    print(cubo[(id1//9)*3:((id1//9)*3)+3,(id1//3*3)%9:(id1//3*3)%9+3,(id1%3*3):(id1%3*3)+3])
    print('')
    print('El cubo con el indice {}\n'.format(id2))
    print(cubo[(id2//9)*3:((id2//9)*3)+3,(id2//3*3)%9:(id2//3*3)%9+3,(id2%3*3):(id2%3*3)+3])
    #cambio de posiciones
    cubo[(id1//9)*3:((id1//9)*3)+3,(id1//3*3)%9:(id1//3*3)%9+3,(id1%3*3):(id1%3*3)+3]=cubo[(id2//9)*3:((id2//9)*3)+3,(id2//3*3)%9:(id2//3*3)%9+3,(id2%3*3):(id2%3*3)+3]
    cubo[(id2//9)*3:((id2//9)*3)+3,(id2//3*3)%9:(id2//3*3)%9+3,(id2%3*3):(id2%3*3)+3]=cuboaux[(id1//9)*3:((id1//9)*3)+3,(id1//3*3)%9:(id1//3*3)%9+3,(id1%3*3):(id1%3*3)+3]
    print('El cubo resultante\n')
    print(cubo)
  
id1= int(input("primer cubo:  "))
id2= int(input("segundo cubo:  "))

cambiarcubo(id1,id2)

    
