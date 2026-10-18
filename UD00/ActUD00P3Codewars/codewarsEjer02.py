def row_sum_odd_numbers(n):
    """
    Calcula la suma de los números impares de una fila del triángulo.

    Parámetros:
        n (int): Número de la fila, empezando desde la fila 1.

    Devuelve:
        int: La suma de los números de la fila.
    """

    # Elevamos el número de la fila al cubo.
    resultado = n ** 3

    # Devolvemos el resultado.
    return resultado


# Probamos la función con diferentes ejemplos.
print("Prueba 1:", row_sum_odd_numbers(1))   # Esperado: 1
print("Prueba 2:", row_sum_odd_numbers(2))   # Esperado: 8
print("Prueba 3:", row_sum_odd_numbers(13))  # Esperado: 2197
print("Prueba 4:", row_sum_odd_numbers(19))  # Esperado: 6859
print("Prueba 5:", row_sum_odd_numbers(41))  # Esperado: 68921