# ejemplos de como funciona los operadores is, not, in

print("Operador is")
a = [1,2,3]
b = a

print(a is b) # devuelve true, apuntan a la misma lista

c = [1,2,3]
d = [1,2,3]
print(c is d) # devuelve false, son lista diferentes
# is comprueba identidad, no igualdad

print("Operador not")

edad = 20

print(edad > 18) # devuelve true
print(not edad > 18) #devuelve false

print("Operador in")

# con lista
frutas = ["manzana","platano","naranja"]
print("manzana" in frutas) #devuelve true
print("pera" in frutas) #devuelve false

# con cadena
nombre = "francisco"
print("fran" in nombre) #devuelve true

