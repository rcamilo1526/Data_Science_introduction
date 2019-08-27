# -*- coding: utf-8 -*-
import numpy as np
#crear arreglo 9x9x9
m1 = np.arange(729).reshape(9,9,9)
a='0:3,0:3,0:3'
m1[[a,1]] = m1[[1,0]]


    
print(m1[0:2])

