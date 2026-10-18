# Importamos math para poder utilizar ceil().
import math


def century(year):
    """
    Calcula el siglo al que pertenece un ano.

    Parametros:
        year (int): Ano que queremos comprobar.

    Devuelve:
        int: Numero del siglo correspondiente.
    """

    # Dividimos el ano entre 100.
    # Utilizamos ceil() para redondear hacia arriba.
    siglo = math.ceil(year / 100)

    # Devolvemos el siglo calculado.
    return siglo


def century2(year):
    """
    Calcula el siglo al que pertenece un ano.

    Parametros:
        year (int): Ano que queremos comprobar.

    Devuelve:
        int: Numero del siglo correspondiente.
    """

    # Sumamos 99 al ano para poder calcular el siglo correctamente.
    # Despues dividimos entre 100 usando division entera.
    siglo = (year + 99) // 100

    # Devolvemos el siglo calculado.
    return siglo


# Probamos la funcion con diferentes ejemplos.
print("Prueba 1:", century(1705))  # Esperado: 18
print("Prueba 2:", century(1900))  # Esperado: 19
print("Prueba 3:", century(1601))  # Esperado: 17
print("Prueba 4:", century(2000))  # Esperado: 20
print("Prueba 5:", century(2742))  # Esperado: 28
print("Prueba 6:", century(100))   # Esperado: 1
print("Prueba 7:", century(101))   # Esperado: 2