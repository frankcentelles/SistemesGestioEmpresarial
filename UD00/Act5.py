# pasar varios parametros de la consola a python

import sys

nombre = sys.argv[1]
edad = sys.argv[2]
ciudad =sys.argv[3]

print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)

# desde la consola
# Fran 20 Valencia

# ejemplo de sobrecarga de funciones

# con diversos numeros como parametros
def suma(a,b=0):
    return a+b

print(suma(5)) #reultado 5
print(suma(5,3)) #resultado 8

# parametro no definido
def suma_varios(*numeros):
    resultado =0

    for numero in numeros:
        resultado = resultado + numero
    return resultado

print(suma_varios(2,3)) #resultado 5
print(suma_varios(2,3,4)) #resultado 9
print(suma_varios(1,2,3,4)) #resultado 15

# ejemplo completo
def suma2(*numeros):
    resultado = 0

    for numero in numeros:
        resultado = resultado + numero

    return resultado


print("Nombre:", sys.argv[1])
print("Suma:", suma(2, 3, 4))