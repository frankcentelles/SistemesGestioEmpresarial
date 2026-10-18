
def no_space(x):
    """
    Elimina todos los espacios de una cadena de texto.

    Parametros:
        x (str): Cadena de texto original

    Devuelve:
        str: Cadena de texto sin espacios
    """

    # replace() sustituye todas las apariciones de un texto por otro
    # En este caso, sustituimos los espacios " " por nada ""
    resultado = x.replace(" ", "")

    # Devolvemos la cadena sin espacios
    return resultado


# Probamos la funcion con diferentes ejemplos
print("Prueba 1:", no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))
# Esperado: 8j8mBliB8gimjB8B8jlB

print("Prueba 2:", no_space("hello world"))
# Esperado: helloworld

print("Prueba 3:", no_space("Hola que tal"))
# Esperado: Holaquetal

print("Prueba 4:", no_space(""))
# Esperado: (cadena vacia)

print("Prueba 5:", no_space("Python"))
# Esperado: Python
