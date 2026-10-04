
# comprueba si se puede colocar una reina en una fila y columna concretas
def esPosicionSegura(columnas, fila, columna):
    # Comprobamos las reinas colocadas en las filas anteriores
    for filaAnterior in range(fila):

        columnaAnterior = columnas[filaAnterior]

        # Comprobamos si comparten columna
        if columnaAnterior == columna:
            return False

        # Comprobamos si comparten una diagonal
        # calcula el valor absoluto de una diferencia 
        if abs(columnaAnterior - columna) == abs(filaAnterior - fila):
            return False

    return True

# funcion recursiva principal
def resolverReinas(n, fila, columnas):
    # Si hemos colocado todas las reinas, encontramos una solucion
    if fila == n:
        return 1

    # Contador de soluciones encontradas
    soluciones = 0

    # Probamos todas las columnas de la fila actual
    for columna in range(n):

        # Comprobamos si la posicion es segura
        if esPosicionSegura(columnas, fila, columna):

            # guarda la columna en la que se encuentra cada reina de cada fila
            columnas[fila] = columna

            # Continuamos con la siguiente fila
            soluciones += resolverReinas(n, fila + 1, columnas)

            # No hace falta borrar la posicion:
            # se sustituira al probar otra columna

    return soluciones

# crea una lista de N posiciones, inicialmente -1
def contarSoluciones(n):
    # Creamos una lista para guardar la columna de cada reina
    columnas = [-1] * n

    # Empezamos a colocar las reinas desde la primera fila
    return resolverReinas(n, 0, columnas)


if __name__ == "__main__":
    try:
        n = int(input("Introduce el numero de reinas (4-10): "))

        # Comprobamos el rango permitido
        if n < 4 or n > 10:
            print("El numero debe estar entre 4 y 10.")
        else:
            # Calculamos las soluciones
            resultado = contarSoluciones(n)

            print("Tablero:", n, "x", n)
            print("Soluciones totales:", resultado)

    except ValueError:
        print("Error: debes introducir un numero entero.")