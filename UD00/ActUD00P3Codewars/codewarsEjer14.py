
def find_outlier(integers):
    """
    Encuentra el unico numero que es diferente al resto
    por ser par o impar.

    Parametros:
        integers (list): Lista de numeros enteros

    Devuelve:
        int: El numero que es diferente al resto
    """

    # Creamos dos listas vacias: una para pares y otra para impares
    pares = []
    impares = []

    # Recorremos todos los numeros de la lista
    for numero in integers:

        # Si el resto de dividir entre 2 es 0, el numero es par
        if numero % 2 == 0:
            pares.append(numero)

        # Si no, el numero es impar
        else:
            impares.append(numero)

    # Si solo hay un numero impar, ese es el diferente
    if len(impares) == 1:
        return impares[0]

    # Si no, el numero diferente es el unico par
    else:
        return pares[0]


# Probamos la funcion con diferentes ejemplos
print("Prueba 1:", find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# Esperado: 11

print("Prueba 2:", find_outlier([160, 3, 1719, 19, 11, 13, -21]))
# Esperado: 160

print("Prueba 3:", find_outlier([1, 3, 5, 7, 8, 9, 11]))
# Esperado: 8

print("Prueba 4:", find_outlier([2, 4, 6, 7, 10, 12]))
# Esperado: 7
