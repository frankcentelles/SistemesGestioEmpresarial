import os
import sys
import cv2
from pyzbar.pyzbar import decode

def leerCodigos(directorio):
    # Comprobamos que la ruta sea un directorio
    if not os.path.isdir(directorio):
        print("Error: el directorio no existe.")
        return

    # Recorremos todos los archivos del directorio
    # obtiene todos los nombres de archivo de la carpeta
    for archivo in os.listdir(directorio):

        # selecciona los archivos PNG, sin distinguir mayusculas
        if archivo.lower().endswith(".png"):
            ruta = os.path.join(directorio, archivo)

            # carga la imagen y la convierte en datos que OpenCV puede procesar
            imagen = cv2.imread(ruta)

            if imagen is None:
                print("No se puede leer:", archivo)
                continue

            # busca codigos de barras reconocibles en la imagen
            codigos = decode(imagen)

            # separa el nombre del archivo de su extension
            nombreAlumno = os.path.splitext(archivo)[0]

            # Comprobamos si se ha detectado algun codigo.
            if len(codigos) == 0:
                print(nombreAlumno, "- No se ha encontrado ningun codigo.")
                continue

            # Recorremos los codigos encontrados.
            for codigo in codigos:
                # contiene la informacion decodificada, que se convierte a texto
                identificador = codigo.data.decode("utf-8")

                print("Alumno:", nombreAlumno)
                print("ID:", identificador)
                print("--------------------")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python Act10parte2.py directorio")
        sys.exit(1)

    leerCodigos(sys.argv[1])
