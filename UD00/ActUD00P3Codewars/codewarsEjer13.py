def expression_matter(a, b, c):
    """
    Devuelve el mayor resultado posible combinando tres numeros
    con sumas, multiplicaciones y parentesis.

    Parametros:
        a (int): Primer numero
        b (int): Segundo numero
        c (int): Tercer numero

    Devuelve:
        int: El mayor resultado posible
    """

    # Calculamos todas las combinaciones posibles
    resultado1 = a + b + c
    resultado2 = a * b * c
    resultado3 = (a + b) * c
    resultado4 = a * (b + c)
    resultado5 = a + b * c
    resultado6 = a * b + c

    # Guardamos todos los resultados en una lista
    resultados = [
        resultado1,
        resultado2,
        resultado3,
        resultado4,
        resultado5,
        resultado6
    ]

    # max() devuelve el numero mas grande de la lista
    mayor = max(resultados)

    # Devolvemos el resultado mas grande
    return mayor


# Probamos la funcion con diferentes ejemplos
print("Prueba 1:", expression_matter(1, 2, 3))
# Esperado: 9

print("Prueba 2:", expression_matter(1, 1, 1))
# Esperado: 3

print("Prueba 3:", expression_matter(9, 1, 1))
# Esperado: 18

print("Prueba 4:", expression_matter(2, 3, 4))
# Esperado: 24

print("Prueba 5:", expression_matter(5, 1, 3))
# Esperado: 20