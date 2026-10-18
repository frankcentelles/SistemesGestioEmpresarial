
def even_or_odd(number):
    """
    Comprueba si un numero es par o impar.

    Parametros:
        number (int): Numero entero que queremos comprobar.

    Devuelve:
        str: "Even" si es par o "Odd" si es impar.
    """

    # El operador % obtiene el resto de una division.
    # Si el resto de dividir entre 2 es 0, el numero es par.
    if number % 2 == 0:
        return "Even"

    # Si no es divisible entre 2, el numero es impar.
    else:
        return "Odd"


# Probamos la funcion con diferentes numeros.
print("Prueba 1:", even_or_odd(4))
# Esperado: Even

print("Prueba 2:", even_or_odd(7))
# Esperado: Odd

print("Prueba 3:", even_or_odd(0))
# Esperado: Even

print("Prueba 4:", even_or_odd(-3))
# Esperado: Odd
