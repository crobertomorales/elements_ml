import numpy as np

A = np.arange(5,9).reshape(2,2)
B = np.arange(-7,-1).reshape(2,3)
C = np.arange(4,14,3).reshape(2,2)
D = np.eye(2)
E = np.zeros(6).reshape(2,3)

parte1 = np.hstack([A,D,E])
parte2 = np.hstack([D,C,B])
F = np.vstack([parte1,parte2])
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
