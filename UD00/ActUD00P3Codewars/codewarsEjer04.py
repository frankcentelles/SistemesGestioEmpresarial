def make_upper_case(s):
    """
    Convierte una cadena de texto a mayusculas.

    Parametros:
        s (str): Cadena de texto que queremos convertir.

    Devuelve:
        str: La cadena convertida a mayusculas.
    """

    # Convertimos todas las letras a mayusculas.
    # Devolvemos el texto convertido.
    return s.upper()


# Probamos la funcion con diferentes ejemplos.
print("Prueba 1:", make_upper_case("hello"))       # Esperado: HELLO
print("Prueba 2:", make_upper_case("hello world")) # Esperado: HELLO WORLD
print("Prueba 3:", make_upper_case("Python"))      # Esperado: PYTHON
print("Prueba 4:", make_upper_case("123abc"))      # Esperado: 123ABC
print("Prueba 5:", make_upper_case(""))            # Esperado: (cadena vacia)