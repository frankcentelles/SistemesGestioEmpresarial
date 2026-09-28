#recibe 2 numeros y devuelve la suma
def suma(num1,num2):
    return num1+num2

result=suma(5,3)

print(result)

# recibe una lista y modifica esa misma lista doblando los valores de todos los elemntos, sin devolver nada
def doblarLista(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] *2

lista=[1,2,3,4]

doblarLista(lista)

print(lista)

# recibe una lista y devuelve una copia de la misma lista doblando los valores, sin modificar la lista original
def doblarLista2(lista):
    copia = lista.copy()

    for i in range(len(copia)):
        copia[i] = copia[i] *2
    
    return copia

print(doblarLista2(lista))