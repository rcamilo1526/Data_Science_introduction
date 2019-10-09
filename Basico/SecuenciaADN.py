# -*- coding: utf-8 -*-

#Raúl Camilo Martín Bernal 20151025909


import random 
#funcion que crea las secuencias aleatorias
def llenadoAleatorio(s,n):
    #crea un string con las letras
    letras='ACGT'
    #llena un string de tamaño n y lo llena con la seleccion aleatoria de letras
    i=0
    while i<n:
        s+=random.choice(letras)
        i+=1
    return s


#Crea dos string para las secuencias
s1='' 
s2=''
#las llena con tamaños 150 y 30 respectivamente
s1=llenadoAleatorio(s1,150)
s2=llenadoAleatorio(s2,30)
#Crea vector vacio para guardar puntuaciónes
VectorPuntaje=[]
#recorre las 150 pusiciones
i=0
while i<150:
    puntuacion=0
    #compara cada posición
    for x in range(30):
        #Si el indice es mayor al tamaño de la secuencia 1 continua a la siguiente comparación
        if (x+i)>149:
            continue
        else: 
            if s1[x+i]==s2[x]:
                puntuacion +=1
    else:
        #añade al vector de puntaje la puntuación
        VectorPuntaje.append(puntuacion)
        i+=1
#guarda las variables del maximo puntaje y su posición
mayor_coincidencia=max(VectorPuntaje)      
mejor_posicion=VectorPuntaje.index(mayor_coincidencia)
#imprime el maximo y su posición
print('La mejor coincidencia es' )
print('la posición {}'.format(mejor_posicion))
print('con un total de {} coincidencias'.format(mayor_coincidencia))
#imprime la primera secuencia poniendo en rojo la mejor secuencia y la segunda se alinea con guiones (-)
print(s1[:mejor_posicion]+"\033[1;31m"+s1[mejor_posicion:mejor_posicion+len(s2)]+'\033[0;m'+s1[mejor_posicion+len(s2):])
#multiplica guiones por el indice de la mejor posición despues imprime la segunda secuencia y despues llena hasta el 150 con guiones
print('-'*mejor_posicion+s2+'-'*(150-mejor_posicion-len(s2)))


        


    



