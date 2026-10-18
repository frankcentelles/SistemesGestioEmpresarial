def string_to_array(string):
    """
    Divide una cadena de texto en una lista de palabras.

    Parametros:
        string (str): Cadena de texto que queremos dividir.

    Devuelve:
        list: Lista con las palabras separadas.
    """

    # Utilizamos split() para separar la cadena por los espacios.
    # El resultado sera una lista con cada palabra.
    palabras = string.split(" ")

    # Devolvemos la lista de palabras.
    return palabras


# Probamos la funcion con diferentes ejemplos.
print("Prueba 1:", string_to_array("string"))
# Esperado: ['string']

print("Prueba 2:", string_to_array("Robin Singh"))
# Esperado: ['Robin', 'Singh']

print("Prueba 3:", string_to_array("I love arrays they are my favorite"))
# Esperado: ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']

print("Prueba 4:", string_to_array("Hola mundo"))
# Esperado: ['Hola', 'mundo']

print("Prueba 5:", string_to_array(""))
# Esperado: []