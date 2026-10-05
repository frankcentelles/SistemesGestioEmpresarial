# recibe un codigo mediante un array bidimensional (de longitud variable) "BUSCAMINAS"
# un 0 donde no haya minas y un -1 donde si
def contandoMinas(miCampo):
    # almacenan el tamaño del campo
    filas = len(miCampo)
    columnas = len(miCampo[0])

    # creamos una nueva matriz
    resultado = []

    # creamos una matriz del mismo tamaño
    for f in range(filas):
        resultado.append([0] *columnas)

    # recorremos todas las casillas
    for f in range(filas):
        for c in range(columnas):

            # si hay una mina, la dejamos como -1
            if miCampo[f][c] == -1:
                resultado[f][c] = -1
            else:
                contador = 0

                # revisamos las 8 casillas vecinas
                # df y dc representan los desplazamientos de fila y columna
                for df in range(-1,2):
                    for dc in range(-1,2):
                        nf = f + df
                        nc = c + dc

                        # comprobamos que la posicion existe
                        # evita acceder a una fila que no existe
                        if 0 <= nf < filas and 0 <= nc < columnas:
                            if miCampo[nf][nc] == -1:
                                contador += 1

                resultado[f][c] = contador

    return resultado

campo = [[0,-1,0],[0,0,0],[-1,0,0]]

for fila in contandoMinas(campo):
    print(fila)
