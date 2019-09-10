# -*- coding: utf-8 -*-


from PIL import Image
import numpy as np
import cv2
import copy

orden=(np.arange(16))
np.random.shuffle(orden)
desorden=copy.deepcopy(orden)
orden.sort()
im=cv2.imread("16.jpg",0)

x= int(im.shape[0]/4)
y= int(im.shape[1]/4)  
im2=np.zeros((x*4,y*4),dtype=int)
im3=np.zeros((x*4,y*4),dtype=int)
j=0
while j<16:
    for i in desorden:
#        print(j,i)
        im2[j//4*x:j//4*x+x,(j%4)*y:(j%4)*y+y]=im[i//4*x:i//4*x+x,(i%4)*y:(i%4)*y+y]
        j+=1

#guarda la nueva imagen y la muestra    
cv2.imwrite('imagendesordenada.jpg',im2)
imagendesordenada = Image.open("imagendesordenada.jpg")
imagendesordenada.show()
print('ordenar otra vez')
i=0
while i<16:
    for j in desorden:
#        print(i,j)
        im3[j//4*x:j//4*x+x,(j%4)*y:(j%4)*y+y]=im2[i//4*x:i//4*x+x,(i%4)*y:(i%4)*y+y]
        i+=1

cv2.imwrite('imagenreordenada.jpg',im3)
imagenreordenada = Image.open("imagenreordenada.jpg")
imagenreordenada.show()

