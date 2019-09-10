# -*- coding: utf-8 -*-
from PIL import Image
import numpy.matlib
import numpy as np
import cv2


def filtro(x):
    #Lee y muestra la imagen con PIL
    imagenoriginal = Image.open("images.jpg")
    imagenoriginal.show()
    
    im=cv2.imread("images.jpg",0)
    #ya con el indicativo 0 lo toma en blanco y negro y se muestra
    cv2.imwrite('imagesbn.jpg',im)
    imagenbn = Image.open("imagesbn.jpg")
    imagenbn.show()
    #crear la nueva matriz a la cual se le van a asignar los valores de imagen
    im2=np.zeros((im.shape[0], im.shape[1]),dtype=int)
    i=0
    #recorrer todas las matriz haciendo una matriz m de los elementos al rededor en caso de estar en una esquina toma como si la imagen continuara
    while i<im2.shape[0]:
        j=0
        while j<im2.shape[1]:
            m=np.array([[im[i-1,j-1],im[i-1,j],im[i-1,(j+1)%im2.shape[1]]],[im[i,j-1],im[i,j],im[i,(j+1)%im2.shape[1]]],[im[(i+1)%im2.shape[0],j-1],im[(i+1)%im2.shape[0],j],im[(i+1)%im2.shape[0],(j+1)%im2.shape[1]]]])
            im2[i,j]=(sum(sum(m*x)))/9
            j+=1
        i+=1
    #guarda la nueva imagen y la muestra    
    cv2.imwrite('imagesf.jpg',im2)
    imagenfinal = Image.open("imagesf.jpg")
    imagenfinal.show()
    
pa=np.array([[-1,-1,-1],[-1,16,-1],[-1,-1,-1]])
pb=np.array([[1,1,1],[1,1,1],[1,1,1]])

filtro(pb)
