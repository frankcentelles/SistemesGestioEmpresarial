from Act5Parte2 import Escuela, Profesor, Alumno

# Creamos una escuela
escuela = Escuela("IES Ejemplo", "Valencia", "María")

# Creamos profesores
profesor1 = Profesor("Ana", "ciencias")
profesor2 = Profesor("Juan", "letras")
profesor3 = Profesor("Pablo", "mixto")

# Añadimos los profesores a la escuela
escuela.anadir_profesor(profesor1)
escuela.anadir_profesor(profesor2)
escuela.anadir_profesor(profesor3)

# Creamos alumnos con su profesor responsable
alumno1 = Alumno("Marcos", "DAM 1", profesor1)
alumno2 = Alumno("Laura", "DAM 1", profesor2)
alumno3 = Alumno("Jorge", "DAM 2", profesor1)

# Añadimos los alumnos a la escuela
escuela.anadir_alumno(alumno1)
escuela.anadir_alumno(alumno2)
escuela.anadir_alumno(alumno3)

# Mostramos los datos de la escuela
print("DATOS DE LA ESCUELA")
escuela.mostrar()

# Mostramos los profesores
print("\nPROFESORES")
escuela.mostrar_profesores()

# Mostramos los alumnos agrupados por curso
print("\nALUMNOS")
escuela.mostrar_alumnos()

# Modificamos un profesor
print("\nMODIFICAR PROFESOR")
escuela.modificar_profesor(profesor1, "Ana García", "mixto")
profesor1.mostrar()

# Buscamos un alumno
print("\nBUSCAR ALUMNO")
alumno_buscado = escuela.buscar_alumno("Laura")

if alumno_buscado is not None:
    alumno_buscado.mostrar()
else:
    print("Alumno no encontrado")

# Modificamos un alumno
print("\nMODIFICAR ALUMNO")
escuela.modificar_alumno(
    alumno2,
    "Laura García",
    "DAM 2",
    profesor3
)

# Eliminamos un alumno
print("\nELIMINAR ALUMNO")
escuela.eliminar_alumno(alumno3)

# Intentamos eliminar un profesor
# No se podrá porque todavía tiene alumnos responsables
print("\nELIMINAR PROFESOR")
if escuela.eliminar_profesor(profesor1):
    print("Profesor eliminado")
else:
    print("No se puede eliminar: tiene alumnos responsables")

# Mostramos el estado final
print("\nESTADO FINAL")
escuela.mostrar()
escuela.mostrar_profesores()
escuela.mostrar_alumnos()
