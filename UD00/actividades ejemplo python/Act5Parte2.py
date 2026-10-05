class Profesor:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def modificar(self, nombre, tipo):
        if tipo in ["ciencias", "letras", "mixto"]:
            self.nombre = nombre
            self.tipo = tipo
            return True
        return False

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Tipo:", self.tipo)

class Alumno:
    def __init__(self, nombre, curso, profesor):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor

    def modificar(self, nombre, curso, profesor):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Curso:", self.curso)
        print("Profesor responsable:", self.profesor.nombre)

class Escuela:
    def __init__(self, nombre, localidad, responsable):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable

        # Lista de profesores de la escuela
        self.profesores = []

        # Diccionario de grupos: cada curso tiene una lista de alumnos
        self.grupos = {}

    def anadir_profesor(self, profesor):
        # Evitamos añadir dos veces el mismo profesor
        if profesor not in self.profesores:
            self.profesores.append(profesor)
            return True
        return False

    def eliminar_profesor(self, profesor):
        # No eliminamos un profesor si tiene alumnos responsables
        for grupo in self.grupos.values():
            for alumno in grupo:
                if alumno.profesor == profesor:
                    return False

        if profesor in self.profesores:
            self.profesores.remove(profesor)
            return True
        return False

    def modificar_profesor(self, profesor, nombre, tipo):
        if profesor in self.profesores:
            return profesor.modificar(nombre, tipo)
        return False

    def anadir_alumno(self, alumno):
        # El profesor responsable debe ser de la escuela
        if alumno.profesor not in self.profesores:
            return False

        # Creamos el grupo si todavía no existe
        if alumno.curso not in self.grupos:
            self.grupos[alumno.curso] = []

        # Añadimos el alumno a su grupo
        if alumno not in self.grupos[alumno.curso]:
            self.grupos[alumno.curso].append(alumno)
            return True

        return False

    def buscar_alumno(self, nombre):
        for grupo in self.grupos.values():
            for alumno in grupo:
                if alumno.nombre == nombre:
                    return alumno
        return None

    def modificar_alumno(self, alumno, nombre, curso, profesor):
        # Comprobamos que el alumno pertenece a la escuela
        if self.buscar_alumno(alumno.nombre) != alumno:
            return False

        # El profesor debe pertenecer a esta escuela
        if profesor not in self.profesores:
            return False

        # Eliminamos al alumno de su grupo anterior
        self.grupos[alumno.curso].remove(alumno)

        # Si el grupo se queda vacío, lo eliminamos
        if len(self.grupos[alumno.curso]) == 0:
            del self.grupos[alumno.curso]

        # Modificamos los datos del alumno
        alumno.modificar(nombre, curso, profesor)

        # Lo añadimos al nuevo grupo
        if curso not in self.grupos:
            self.grupos[curso] = []

        self.grupos[curso].append(alumno)
        return True

    def eliminar_alumno(self, alumno):
        if alumno.curso in self.grupos:
            if alumno in self.grupos[alumno.curso]:
                self.grupos[alumno.curso].remove(alumno)

                # Eliminamos el grupo si ya no tiene alumnos
                if len(self.grupos[alumno.curso]) == 0:
                    del self.grupos[alumno.curso]

                return True
        return False

    def mostrar_profesores(self):
        for profesor in self.profesores:
            profesor.mostrar()
            print("----------------")

    def mostrar_alumnos(self):
        for curso, grupo in self.grupos.items():
            print("Grupo:", curso)

            for alumno in grupo:
                alumno.mostrar()
                print("----------------")

    def mostrar(self):
        print("Escuela:", self.nombre)
        print("Localidad:", self.localidad)
        print("Responsable:", self.responsable)
        print("Número de profesores:", len(self.profesores))
        print("Número de grupos:", len(self.grupos))
