import numpy as np

m = np.array([
    [1,1,0,0,0,0,1],
    [0,1,1,0,0,1,0],
    [0,0,1,1,0,0,0],
    [0,0,0,1,1,0,1],
    [1,0,0,0,0,1,1],
    [0,0,0,0,1,1,1],
    [1,1,1,0,0,0,1]])

m1 = np.array([
    [1,1,0,0,0,1,1],
    [1,1,1,0,1,0,0],
    [0,1,1,1,1,0,0],
    [0,0,1,1,0,0,1],
    [0,1,1,0,1,1,1],
    [1,0,0,0,1,1,1],
    [1,0,0,1,1,1,1]])

m2 = np.array([
    [1,1,0,0,0,0,0],
    [1,1,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0],
    [0,0,0,0,1,1,1],
    [0,0,0,0,1,1,1],
    [0,0,0,0,1,1,1]])

def reflexiva(m):
    if (np.diagonal(m).sum() == m.shape[0]):
        print("La relación R si es reflexiva")
    else:
        print("La relación R no es reflexiva")

#reflexiva(m)
#reflexiva(m1)
#reflexiva(m2)


def simetrica(m):
    if ((m == np.transpose(m)).all()):
        print("La relación R si es simétrica")
    else:
        print("La relación R no es simétrica")
#simetrica(m)
#simetrica(m1)
#simetrica(m2)

def transitiva(m):
    mm = m.dot(m)
    mm[mm>1] = 1
    if ((m == mm).all()):
        print("La relación R si es transitiva")
    else:
        print("La relación R no es transitiva")
transitiva(m)
transitiva(m1)
transitiva(m2)