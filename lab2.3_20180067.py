# Problema 3 
import numpy as np

A = np.arange(0,24).reshape(4,6)
print(A)

def rotar90(a): 
    x = np.flip(a,-1)
    print('Rotar 90 grados \n', x)

def rotar180(a): 
    y = np.flip(a)
    print('Rotar 180 grados \n', y)

def rotar270(a):
    z = np.flip(a,0)
    z = np.transpose(z)
    print('Rotar 270 grados \n', z)

rotar90(A)
rotar180(A)
rotar270(A)
