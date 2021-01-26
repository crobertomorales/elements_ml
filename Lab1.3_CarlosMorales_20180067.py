#Ejercicio 3
def rombo(pisos0):
    pisos = round((pisos0 / 2) + 0.5)
    pisos2 = round((pisos0 / 2) - 0.5)
    resultado = ''
    for i in range(pisos):
        no_espacios_inicial = pisos - i - 1
        no_ast = i + 1
        resultado += ' ' * no_espacios_inicial + '* ' * no_ast + '\n'
    for i in range(pisos2,0,-1):
        no_espacios_inicial2 = pisos2-i+1
        no_ast2 = i
        resultado += ' ' * no_espacios_inicial2 + '* ' * no_ast2 + '\n'
    return(resultado)

print(rombo(7))
print(rombo(9))
print(rombo(11))