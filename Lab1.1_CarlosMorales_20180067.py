
#Ejercicio 1        
def triangulo(pisos):
    resultado = ''
    for i in range(pisos,0,-1):
        no_espacios_inicial = pisos-i
        no_ast = i
        resultado += ' ' * no_espacios_inicial + '* ' * no_ast + '\n'
    return(resultado)

print(triangulo(4))
print(triangulo(5))
print(triangulo(6))