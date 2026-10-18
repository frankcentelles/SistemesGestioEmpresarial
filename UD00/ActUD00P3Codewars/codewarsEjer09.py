
def square_sum(numbers):
    """
    Eleva al cuadrado cada numero de la lista y suma los resultados.

    Parametros:
        numbers (list): Lista de numeros

    Devuelve:
        int: Suma de los cuadrados de los numeros
    """

    # Creamos una variable para acumular la suma
    suma = 0

    # Recorremos todos los numeros de la lista
    for numero in numbers:

        # Elevamos el numero al cuadrado y lo sumamos
        suma = suma + numero ** 2

    # Devolvemos el resultado final
    return suma


# Probamos la funcion con diferentes ejemplos
print("Prueba 1:", square_sum([1, 2, 2]))
# Esperado: 9 (1² + 2² + 2² = 9)

print("Prueba 2:", square_sum([1, 2, 3]))
# Esperado: 14 (1² + 2² + 3² = 14)

print("Prueba 3:", square_sum([5, 3, 4]))
# Esperado: 50 (5² + 3² + 4² = 50)

print("Prueba 4:", square_sum([]))
# Esperado: 0 (la lista esta vacia)
