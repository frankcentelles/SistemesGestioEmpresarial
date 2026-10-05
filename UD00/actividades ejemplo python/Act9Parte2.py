import csv
import sys
import os
import barcode
from barcode.writer import ImageWriter

def generarCodigos(archivoCSV):
    # Comprobamos que el archivo exista.
    if not os.path.isfile(archivoCSV):
        print("Error: el archivo CSV no existe.")
        return

    # Abrimos el CSV para leer los datos.
    with open(archivoCSV, "r", encoding="utf-8-sig", newline="") as fichero:
        # lee el csv utilizando los nombre de las columnas
        lector = csv.DictReader(fichero)

        # Comprobamos que existan las columnas necesarias.
        if lector.fieldnames is None or "nombre" not in lector.fieldnames or "ID" not in lector.fieldnames:
            print("Error: el CSV debe contener las columnas nombre e ID.")
            return

        # Recorremos los alumnos.
        for alumno in lector:
            nombre = alumno["nombre"].strip()
            identificador = alumno["ID"].strip()

            # Comprobamos que los datos no esten vacios.
            if nombre == "" or identificador == "":
                print("Alumno con datos incompletos. Se omite.")
                continue

            # El ID debe contener unicamente numeros.
            if not identificador.isdigit():
                print("ID no valido para:", nombre)
                continue

            # EAN13 necesita 12 digitos de entrada.
            if len(identificador) > 12:
                print("ID demasiado largo para:", nombre)
                continue

            # Completamos el ID con ceros a la izquierda.
            codigo = identificador.zfill(12)

            # Creamos el objeto de codigo de barras.
            ean = barcode.get("ean13", codigo, writer=ImageWriter())

            # Evitamos caracteres no permitidos en el nombre.
            nombreArchivo = "".join(
                caracter if caracter.isalnum() or caracter in " _-" else "_"
                for caracter in nombre
            )

            # Generamos el archivo PNG.
            ean.save(nombreArchivo)

            print("Codigo generado:", nombreArchivo + ".png")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python Act9Parte2.py alumnos.csv")
        sys.exit(1)

    generarCodigos(sys.argv[1])
