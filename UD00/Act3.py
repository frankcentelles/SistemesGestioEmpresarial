# almacenar un usuario y su contraseña
# utilizando una lista
import hashlib
# pasar a un formato hash
def hashContraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

#lista de usuarios
usuarios = [] 
# añadimos 5 usuarios y sus contraseñas
usuarios.append(["kike", hashContraseña("1234")])
usuarios.append(["maria", hashContraseña("abcd")])
usuarios.append(["joan", hashContraseña("hola123")])
usuarios.append(["laura", hashContraseña("qwerty")])
usuarios.append(["pepe", hashContraseña("password")])

# consulta 1
usuarioBuscado = "maria"

for usuario in usuarios:
    if usuario[0] == usuarioBuscado:
        print("Usuario: ",usuario[0])
        print("Contraseña hash: ",usuario[1])

# consulta 2
usuarioBuscado2 = "pepe"

for usuario in usuarios:
    if usuario[0] == usuarioBuscado2:
        print("Usuario: ",usuario[0])
        print("Contraseña hash: ",usuario[1])


# utilizando un diccionario
def hashContraseña2(contrasenya):
    return hashlib.sha256(contrasenya.encode()).hexdigest()

#diccionario de usuarios
usuarios2 = {}

# añadimos 5 usuarios y sus contraseñas
usuarios2["kike"] = hashContraseña2("1234")
usuarios2["maria"] = hashContraseña2("abcd")
usuarios2["joan"] = hashContraseña2("hola123")
usuarios2["laura"] = hashContraseña2("qwerty")
usuarios2["pepe"] = hashContraseña2("password")

# consulta 1
if usuarioBuscado in usuarios2:
    print("Usuario: ", usuarioBuscado)
    print("Contraseña hash: ", usuarios2[usuarioBuscado])
# consulta 2
if usuarioBuscado2 in usuarios2:
    print("Usuario: ", usuarioBuscado2)
    print("Contraseña hash: ", usuarios2[usuarioBuscado])
