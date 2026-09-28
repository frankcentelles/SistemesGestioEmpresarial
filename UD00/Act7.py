import random

class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color

    def imprimir(self):
        print("Matricula: ",self.matricula)
        print("Color: ",self.color)

    def canviar_color(self,color):
        self.color = color
    
    def es_rojo(self):
        return self.color == "red"

# nombre de coches

n = int(input("Cuantos coches quieres crear? "))

colores = ["red","white","black","blue","pink"]

coches = []

# creamos los coches
for i in range(n):
    matricula = i + 1
    color = random.choice(colores)
    coche = Car(matricula,color)
    coches.append(coche)

# imprimir las 10 primeras instancias
cantidad = min(n,10)

for i in range(cantidad):
    print("Coche",i+1)
    coches[i].imprimir()
    print()

# solo mostrara los 10 primeros coches creados