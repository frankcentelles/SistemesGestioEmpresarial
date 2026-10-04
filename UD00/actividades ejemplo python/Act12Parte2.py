import sys
import pytesseract
from PIL import Image, ImageFilter, ImageOps


def reconocerTexto(rutaImagen):
    # Abrimos la imagen mediante Pillow
    imagen = Image.open(rutaImagen)

    # Convertimos la imagen a escala de grises
    imagen = ImageOps.grayscale(imagen)

    # Aumentamos la nitidez de los caracteres
    imagen = imagen.filter(ImageFilter.SHARPEN)

    # Configuramos el idioma español y el modo de reconocimiento
    # enviamos la imagen procesada al motor OCR 
    # devuelve el texto reconocido
    texto = pytesseract.image_to_string(
        imagen,
        # idioma español spa
        lang="spa", 
        # indica a Tesseract que trate la imagen como un bloque uniforme de texto
        config="--psm 6"
    )

    return texto

if __name__ == "__main__":
    # Comprobamos que se haya indicado una imagen
    if len(sys.argv) != 2:
        print("Uso: python Act12Parte2.py imagen.png")
        sys.exit(1)

    try:
        resultado = reconocerTexto(sys.argv[1])

        print("Texto reconocido:")
        print(resultado)

    except FileNotFoundError:
        print("Error: no se encuentra la imagen.")

    except pytesseract.TesseractNotFoundError:
        print("Error: no se encuentra Tesseract OCR.")

