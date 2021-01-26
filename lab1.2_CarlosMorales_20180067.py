#Ejercicio 2
def ope(n,m):
    total = 0
    if (n <= m):
        total += 1
    if (m == 0):
        total += 1
    if ((n > m) and (m > 0)):
        total += ope(n-1,m) + ope(n-1,m-1)
    return(total)

print(ope(13,7))
print(ope(25,17))

# La funcion se tarda demasiado en correr con inputs tan grandes, no se recomienda correr 50,35 ni 100,85
#print(ope(50,35))
#print(ope(100,85))
