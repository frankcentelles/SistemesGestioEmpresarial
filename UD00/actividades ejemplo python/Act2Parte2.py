# aplicacion que comprueba si una solucion de un sudoku es correcta o no
def esSudokuCorrecto(miArrayBi):
    # crea un conjunto con los numeros del 1 al 9, no guarda valores repetidos
    numeros = set(range(1, 10))

    # Comprobamos que haya 9 filas y 9 columnas
    if len(miArrayBi) != 9:
        return False

    for fila in miArrayBi:
        if len(fila) != 9 or set(fila) != numeros:
            return False

    # Comprobamos las columnas
    for columna in range(9):
        valores = []

        for fila in range(9):
            valores.append(miArrayBi[fila][columna])

        if set(valores) != numeros:
            return False

    # Comprobamos los cuadrados de 3x3
    for inicio_fila in range(0, 9, 3):
        for inicio_columna in range(0, 9, 3):
            valores = []

            for fila in range(inicio_fila, inicio_fila + 3):
                for columna in range(inicio_columna, inicio_columna + 3):
                    valores.append(miArrayBi[fila][columna])

            if set(valores) != numeros:
                return False

    return True

# Leemos el archivo
sudoku = []

with open("Sudoku.in", "r") as archivo:
    for linea in archivo:
        fila = list(map(int, linea.split()))
        sudoku.append(fila)

# Comprobamos el Sudoku
if esSudokuCorrecto(sudoku):
    print("El Sudoku es correcto")
else:
    print("El Sudoku no es correcto")
