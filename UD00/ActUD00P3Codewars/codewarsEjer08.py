def repeat_str(repeat, string):
    """
    Repite una cadena de texto un numero determinado de veces

    Parametros:
        repeat (int): Numero de veces que se repite la cadena
        string (str): Cadena de texto que queremos repetir

    Devuelve:
        str: Cadena de texto repetida.
    """

    # Creamos una cadena vacia para guardar el resultado
    result = ""

    # Repetimos el bucle tantas veces como indique repeat
    for i in range(repeat):

        # Añadimos la cadena al resultado en cada vuelta
        result += string

    # Devolvemos la cadena repetida
    return result


# Probamos la funcion con diferentes ejemplos
print("Prueba 1:", repeat_str(6, "I"))
# Esperado: IIIIII

print("Prueba 2:", repeat_str(5, "Hello"))
# Esperado: HelloHelloHelloHelloHello

print("Prueba 3:", repeat_str(3, "Hola "))
# Esperado: Hola Hola Hola

print("Prueba 4:", repeat_str(1, "Python"))
# Esperado: Python

print("Prueba 5:", repeat_str(0, "Adios"))
# Esperado: (cadena vacia)