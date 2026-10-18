def summation(num):
    """
    Calcula la suma de todos los numeros desde 1 hasta num,
    incluyendo ambos numeros.

    Parametros:
        num (int): Numero hasta el que queremos sumar

    Devuelve:
        int: Resultado de sumar todos los numeros desde 1 hasta num
    """

    # Creamos una variable para guardar la suma
    suma = 0

    # Recorremos todos los numeros desde 1 hasta num
    # El +1 hace que tambien se incluya num.
    for i in range(1, num + 1):

        # Sumamos el numero actual al resultado acumulado
        suma = suma + i

    # Devolvemos la suma total
    return suma


# Probamos la funcion con diferentes ejemplos.
print("Prueba 1:", summation(2))   # Esperado: 3 (1 + 2)
print("Prueba 2:", summation(8))   # Esperado: 36
print("Prueba 3:", summation(1))   # Esperado: 1
print("Prueba 4:", summation(10))  # Esperado: 55
print("Prueba 5:", summation(5))   # Esperado: 15