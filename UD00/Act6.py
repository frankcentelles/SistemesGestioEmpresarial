# lista en el cual cada elemento sea de dos valores, mida y pes
personas =[[175, 70],
    [180, 75],
    [175, 65],
    [190, 80],
    [180, 68],
    [170, 60]]

# key function
# recive una persona de la lista y devuelve una dupla con los valores a utilizar

def criterio(persona):
    return (-persona[0],persona[1])
# para ordenar cada elemento utiliza el resultado de la funcion criterio()
personas.sort(key=criterio)

print(personas)