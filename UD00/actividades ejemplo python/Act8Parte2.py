import os
import shutil

def organizarArchivos():
    # Lista de extensiones que queremos organizar
    extensiones = ["png", "mp4", "doc"]

    # Obtenemos la carpeta actual desde la que se ejecuta el programa
    carpetaActual = os.getcwd()

    # Recorremos todas las extensiones de la lista
    for extension in extensiones:

        # une rutas correctamente, independientemente del SO
        carpetaDestino = os.path.join(carpetaActual, extension)

        # Si la carpeta no existe, la creamos
        if not os.path.exists(carpetaDestino):
            os.mkdir(carpetaDestino) # crea la carpeta

        # devuelve los nombres de los elementos que hay en esa carpeta
        for archivo in os.listdir(carpetaActual):

            # Construimos la ruta completa del archivo.
            rutaArchivo = os.path.join(carpetaActual, archivo)

            # permite distinguir archivos de carpetas
            if os.path.isfile(rutaArchivo):

                # Obtenemos la extension sin distinguir mayusculas.
                # separa la extension del nombre
                extensionArchivo = os.path.splitext(archivo)[1] 
        # convertimos la extension a minusculas y eliminamos el punto
                extensionArchivo = extensionArchivo.lower().lstrip(".")

                # Comprobamos si coincide con la extension buscada.
                if extensionArchivo == extension:

                    # Creamos la ruta de destino.
                    rutaDestino = os.path.join(carpetaDestino, archivo)

                    # Evitamos sobrescribir archivos existentes.
                    if not os.path.exists(rutaDestino):
                        # movemos el archivo a su nueva ubicacion
                  shutil.move(rutaArchivo, rutaDestino) 
                        print("Movido:", archivo, "->", carpetaDestino)
                    else:
                        print("Ya existe el archivo:", archivo)

if __name__ == "__main__":
    organizarArchivos()
    print("Organizacion terminada.")
