# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import cv2


#Lee y muestra la imagen con PIL
imagenoriginal = Image.open("descarga.jpg")
imagenoriginal.show()
## sobra desde aquí
#Vuelve a blanco y negro
imbn=imagenoriginal
i=0
while i<imagenoriginal.size[0]:
    j=0
    while j<imbn.size[1]:
        r,g,b=imbn.getpixel((i,j))
        g=(r+g+b)/3
        gris=int(g)
        pixel=tuple([gris,gris,gris])
        imbn.putpixel((i,j),pixel)
        j+=1
    i+=1
imbn.show()

#Sin necesidad de volverla b/n OpenCV ya lo convierte en blanco y negro para trabajarlo
## hasta aquí
im=cv2.imread("descarga.jpg",0)
#crear la nueva matriz a la cual se le van a asignar los valores de imagen
im2=np.zeros((im.shape[0], im.shape[1]),dtype=int)
i=0
#recorrer todas las matriz haciendo una matriz m de los elementos al rededor en caso de estar en una esquina toma como si la imagen continuara
while i<im2.shape[0]:
    j=0
    while j<im2.shape[1]:
        m=np.array([[im[i-1,j-1],im[i-1,j],im[i-1,(j+1)%im2.shape[1]]],[im[i,j-1],im[i,j],im[i,(j+1)%im2.shape[1]]],[im[(i+1)%im2.shape[0],j-1],im[(i+1)%im2.shape[0],j],im[(i+1)%im2.shape[0],(j+1)%im2.shape[1]]]])
        im2[i,j]=np.mean(m)
        j+=1
    i+=1
#guarda la nueva imagen y la muestra    
cv2.imwrite('Escudo-de-Colombiafiltrada.jpg',im2)
imagenfinal = Image.open("Escudo-de-Colombiafiltrada.jpg")
imagenfinal.show()
