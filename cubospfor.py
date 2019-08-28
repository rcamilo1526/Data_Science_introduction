# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:29:36 2019

@author: Usuario
"""

import numpy as np
import copy
 

cubo = np.arange(729).reshape(9,9,9)
cuboaux = copy.deepcopy(cubo)

def obtenercubo(id1,x,y,z):
    if(id1<27):
        
        a = [x,y,z]
        if(id1>0):
            if(x<6):
                x=x+3
                if(y>8):
                    y=0
                            
                a = obtenercubo(id1-1,x,y,z)
                               
            else:
                x=0
                y=y+3
                if(y>8):
                    y=0
                    z=z+3
                    
                a = obtenercubo(id1-1,x,y,z)
                    
              
        return a
    

def cambiarcubo(id1,id2):
    global cuboaux
    a = obtenercubo(id1,0,0,0)
    b = obtenercubo(id2,0,0,0)
    
    cubo[a[2]:a[2]+3,a[1]:a[1]+3,a[0]:a[0]+3]= cubo[b[2]:b[2]+3,b[1]:b[1]+3,b[0]:b[0]+3]
    cubo[b[2]:b[2]+3,b[1]:b[1]+3,b[0]:b[0]+3]= cuboaux[a[2]:a[2]+3,a[1]:a[1]+3,a[0]:a[0]+3]
    cuboaux = copy.deepcopy(cubo)
    print(cubo)

a= int(input("primer cubo:  "))
b= int(input("segundo cubo:  "))
cambiarcubo(a,b)
    
    
