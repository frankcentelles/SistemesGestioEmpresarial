from Act6Parte2 import Escuela, Profesor, Alumno, Session

with Session() as session:
    # Buscamos la escuela en la base de datos
    escuela = session.query(Escuela).filter_by(nombre="IES Fausti").first()

    # Si no existe, la creamos
    if escuela is None:
        escuela = Escuela(nombre="IES Fausti")
        session.add(escuela)

        profesor = Profesor(
            nombre="Anna",
            dni="111A",
            especialidad="Python"
        )

        alumno = Alumno(
            nombre="Pau",
            dni="222B",
            curso="DAM"
        )

        escuela.profesores.append(profesor)
        escuela.alumnos.append(alumno)

        session.commit()

    # Leemos los datos guardados
    print("Escuela:", escuela.nombre)

    for profesor in escuela.profesores:
        print(profesor.nombre, profesor.dni, profesor.especialidad)

    for alumno in escuela.alumnos:
        print(alumno.nombre, alumno.dni, alumno.curso)
