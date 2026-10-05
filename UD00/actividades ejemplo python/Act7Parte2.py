import sys
import doctest

def esPalindromo(numero):
    """
    Comprueba si un numero es palindromo.

    >>> esPalindromo(121)
    True
    >>> esPalindromo(123)
    False
    >>> esPalindromo(7)
    True
    >>> esPalindromo(-121)
    False
    """
    texto = str(numero)

    # Los numeros negativos no se consideran palindromos.
    if numero < 0:
        return False

    # Invertimos el texto y lo comparamos con el original.
    return texto == texto[::-1]

def esPrimo(numero):
    """
    Comprueba si un numero es primo.

    >>> esPrimo(7)
    True
    >>> esPrimo(10)
    False
    >>> esPrimo(2)
    True
    >>> esPrimo(1)
    False
    >>> esPrimo(-5)
    False
    """
    # Los numeros menores que 2 no son primos.
    if numero < 2:
        return False

    # Solo es necesario probar divisores hasta la raiz cuadrada.
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False

    return True

def procesarFicheros(entrada, salida):
    # Abrimos el archivo de entrada en modo lectura.
    with open(entrada, "r", encoding="utf-8") as fichero:
        numeros = []

        # Leemos cada linea del archivo.
        for linea in fichero:
            linea = linea.strip()

            # Ignoramos las lineas vacias.
            if linea != "":
                numeros.append(int(linea))

    # Contadores de los numeros que cumplen cada condicion.
    cantidadPalindromos = 0
    cantidadPrimos = 0

    # Lista de numeros que son primos y palindromos.
    resultado = []

    # Analizamos todos los numeros leidos.
    for numero in numeros:
        palindromo = esPalindromo(numero)
        primo = esPrimo(numero)

        if palindromo:
            cantidadPalindromos += 1

        if primo:
            cantidadPrimos += 1

        if palindromo and primo:
            resultado.append(numero)

    # Abrimos el archivo de salida en modo escritura.
    with open(salida, "w", encoding="utf-8") as fichero:
        fichero.write(
            f"Hi han {cantidadPalindromos} numeros palindromos.\n"
        )
        fichero.write(
            f"Hi han {cantidadPrimos} numeros primos.\n"
        )

        # Escribimos un numero por linea.
        for numero in resultado:
            fichero.write(str(numero) + "\n")

if __name__ == "__main__":
    # Ejecutamos primero las pruebas unitarias.
    resultadoTests = doctest.testmod()

    # Comprobamos que se han recibido los dos parametros.
    if len(sys.argv) != 3:
        print("Uso: python Act7Parte2.py entrada.txt salida.txt")
        sys.exit(1)

    try:
        procesarFicheros(sys.argv[1], sys.argv[2])
        print("Archivo de salida generado correctamente.")
    except ValueError:
        print("Error: el archivo contiene un valor que no es un entero.")
    except FileNotFoundError:
        print("Error: no se ha encontrado el archivo de entrada.")
