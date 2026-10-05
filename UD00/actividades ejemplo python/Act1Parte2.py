# explicacion y ejemplos de funciones lambda
# ejemplo de funcion lambda
sumar = lambda a, b: a + b

from functools import reduce

# pedimos numeros separados por espacios
entrada = input("Introduce numeros separados por espacios: ")

# convertimos el texto en una lista de numeros enteros
numeros = list(map(int,entrada.split()))

# filttramos los numeros mayores o iguales que 10
mayores = list(filter(lambda x: x >= 10, numeros))

# multiplicamos todos los numeros filtrados
if len(mayores) > 0:
    producto = reduce(lambda a,b: a * b, mayores)
else:
    producto = 0

print("Lista original: ",numeros)
print("Numeros mayores o iguales que 10: ",mayores)
print("Producto: ",producto)
