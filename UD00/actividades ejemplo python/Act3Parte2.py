# contar cuantas veces aparecen los patrones en una cadena de texto
def numeroPatrones(text):
    patrones = ["00","101","ABC","HO"]

    # pasamos todo el texto a mayusculas
    texto = text.upper()

    resultados = {}

    for patron in patrones:
        contador = 0

        # recorremos todas las posiciones posibles
        # len(texto) devuelve el número de caracteres
        for i in range(len(texto) - len(patron) + 1):
            # texto[i:i + len(patron)] extrae un fragmento del
            # texto del mismo tamaño que el patrón.
            if texto[i:i + len(patron)] == patron:
                contador += 1

        resultados[patron] = contador

    return resultados

frase = input("Introduce un texto: ")

resultado = numeroPatrones(frase)

# recorremos los patrones con las veces q aparece cada uno
for patron, cantidad in resultado.items():
    print(patron,"aparece",cantidad,"veces")
