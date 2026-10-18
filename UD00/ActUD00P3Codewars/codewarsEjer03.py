def past(h, m, s):
    """
    Calcula los milisegundos transcurridos desde la medianoche.

    Parametros:
        h (int): Numero de horas.
        m (int): Numero de minutos.
        s (int): Numero de segundos.

    Devuelve:
        int: Tiempo transcurrido en milisegundos.
    """

    # Convertimos las horas a milisegundos.
    horas_ms = h * 60 * 60 * 1000

    # Convertimos los minutos a milisegundos.
    minutos_ms = m * 60 * 1000

    # Convertimos los segundos a milisegundos.
    segundos_ms = s * 1000

    # Sumamos los milisegundos de las horas, minutos y segundos.
    resultado = horas_ms + minutos_ms + segundos_ms

    # Devolvemos el resultado final.
    return resultado


# Probamos la funcion con diferentes ejemplos.
print("Prueba 1:", past(0, 1, 1))       # Esperado: 61000
print("Prueba 2:", past(0, 0, 0))       # Esperado: 0
print("Prueba 3:", past(1, 0, 0))       # Esperado: 3600000
print("Prueba 4:", past(0, 1, 0))       # Esperado: 60000
print("Prueba 5:", past(1, 1, 1))       # Esperado: 3661000
print("Prueba 6:", past(23, 59, 59))    # Esperado: 86399000