print("clonar lista")

llista = [1, 2, 3, 4]

copia = llista.copy()

print(copia)

# diferencia entre shallow copy y deep copy
# shallow copy, copia la lista exterior pero los elementos interiores continuan sindo compartidos
print("shallow copy")
import copy

llista = [1, 2, 3, 4]

copia = copy.copy(llista)

print(llista)
print(copia)

# deep copy crea una copia completa incluyendo las listas interiores
print("deep copy")
import copy

lista2 = [1,2,3,4]
copia2 = copy.deepcopy(lista2)

print(lista2)
print(copia2)

print("afegir un element a la llista")

llista.append(4)
print(llista)
# seleccionamos la posicion (posicion, objeto)
llista.insert(0,0)
print(llista)

print("llevar un element de la lista")

llista.remove(3)
print(llista)

# eliminamos segun la posicion
llista.pop(2)
print(llista)

# crear una nova llista amb el 4 ultims elemtes de la llista
print("nueva lista con los ultimos 4 elemntos de la lista")
llista2 = [1,2,3,4,5,6,7]
nuevaLlista=llista2[-4:]
print(nuevaLlista)

# convertir les paraules d'una cadena a una llista
cadena1 = "hola esto es una cadena"
lista3 = cadena1.split()
print("lista en cadena: "+lista3)

# comentaris amb una linea


# comentaris multilinea
"""
hola
"""
