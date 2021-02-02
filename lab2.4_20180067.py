import numpy as np

sistema = np.array([[2,0,0,1,0,0,0,0],
[1,0,0,1,0,0,0,0],[-1,0,0,2,0,0,0,0],
[0,2,0,0,1,0,0,0],[0,1,0,0,1,0,0,0],
[0,-1,0,0,2,0,0,0],[0,0,2,0,0,1,0,0],
[0,0,1,0,0,1,0,0],[0,0,-1,0,0,2,0,0],
[0,0,0,0,0,0,1,2],[0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,2,-1]])

derecha = np.array([[4],[3],[3],[3],[2],[1],[6],[4],[2]
,[-3],[-1],[4]])

solucion =  np.linalg.pinv(sistema).dot(derecha)
variables = np.array(["x","y","z","a","b","c","d","t"])


print(np.transpose(variables), np.transpose(solucion))

