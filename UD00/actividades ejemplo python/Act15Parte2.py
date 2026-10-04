import sys
import time
import os
import re
import pyperclip

# recibe la ruta del archivo y lee todas las palabras prohibidas
def cargarPalabras(ruta):
    # Comprobamos que el archivo exista
    if not os.path.isfile(ruta):
        raise FileNotFoundError("No se encuentra el archivo.")

    # Lista donde guardaremos las palabras prohibidas
    palabras = []

    # Abrimos el archivo en modo lectura
    with open(ruta, "r", encoding="utf-8") as fichero:
        for linea in fichero:
            # elimina los espacios sobrantes y los saltos de linea
            # guarda las palabras en una lista que se devuelve al programa principal
            palabra = linea.strip()

            # Ignoramos las lineas vacias
            if palabra != "":
                palabras.append(palabra)

    return palabras

# recibe el texto que se ha copiado y la lista de palabras prohibidas
def filtrarTexto(texto, palabras):
    # Recorremos todas las palabras prohibidas
    for palabra in palabras:

        # Creamos una expresion regular segura
        # para que los caracteres especiales de una palabra
        # se interpreten literalmente dentro de la expresión regular
        patron = re.escape(palabra)

        # Sustituimos cada caracter de la palabra por un asterisco
        # busca las coincidencias y las sustituye por una cantidad
        # de asteriscos igual a la longitud de la coincidencia
        texto = re.sub(
            patron,
            lambda coincidencia: "*" * len(coincidencia.group()),
            texto,
            # para que no se distinga entre mayúsculas y minúsculas
            flags=re.IGNORECASE
        )

    return texto

# comprueba continuamente el portapapeles
def supervisarPortapapeles(palabras):
    # obtenemos y guardamos el contenido inicial
    ultimoTexto = pyperclip.paste()

    print("Programa iniciado.")
    print("Copia un texto para filtrar las palabras.")
    print("Pulsa Ctrl+C para terminar.")

    try:
        while True:
            # Leemos el contenido actual del portapapeles
            texto = pyperclip.paste()

            # Comprobamos si ha cambiado
            if texto != ultimoTexto:

                # Filtramos el texto copiado
                textoFiltrado = filtrarTexto(texto, palabras)

                # Solo modificamos el portapapeles si hay cambios
                if textoFiltrado != texto:
                    # vuelve a copiar el texto modificado
                    pyperclip.copy(textoFiltrado)
                    print("Texto filtrado:", textoFiltrado)

                # Actualizamos el ultimo contenido procesado
                ultimoTexto = textoFiltrado

            # Esperamos antes de volver a comprobar
            time.sleep(0.5)

    # permite finalizar el programa mediante Ctrl+C
    except KeyboardInterrupt:
        print("\nPrograma finalizado.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python Act15Parte2.py lista.txt")
        sys.exit(1)

    try:
        palabras = cargarPalabras(sys.argv[1])

        if len(palabras) == 0:
            print("El archivo no contiene palabras prohibidas.")
        else:
            supervisarPortapapeles(palabras)

    except FileNotFoundError as error:
        print("Error:", error)

