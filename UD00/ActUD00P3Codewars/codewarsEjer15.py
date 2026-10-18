
def solution(n):
    """
    Convierte un numero entero en numeros romanos.

    Parametros:
        n (int): Numero entero entre 1 y 3999

    Devuelve:
        str: Representacion del numero en numeros romanos
    """

    # Guardamos los valores romanos de mayor a menor
    valores = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]

    # Guardamos los simbolos romanos correspondientes
    simbolos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]

    # Creamos una cadena vacia para construir el resultado
    romano = ""

    # Recorremos los valores romanos de mayor a menor
    for i in range(len(valores)):

        # Mientras el numero sea mayor o igual al valor actual...
        while n >= valores[i]:

            # Añadimos el simbolo romano al resultado
            romano = romano + simbolos[i]

            # Restamos al numero el valor que acabamos de utilizar
            n = n - valores[i]

    # Devolvemos el numero romano completo
    return romano


# Probamos la funcion con diferentes ejemplos
print("Prueba 1:", solution(1))
# Esperado: I

print("Prueba 2:", solution(4))
# Esperado: IV

print("Prueba 3:", solution(9))
# Esperado: IX

print("Prueba 4:", solution(1000))
# Esperado: M

print("Prueba 5:", solution(1666))
# Esperado: MDCLXVI

print("Prueba 6:", solution(1990))
# Esperado: MCMXC

print("Prueba 7:", solution(2008))
# Esperado: MMVIII

print("Prueba 8:", solution(3999))
# Esperado: MMMCMXCIX
