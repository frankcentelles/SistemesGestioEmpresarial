from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

class Base(DeclarativeBase):
    pass

class Escuela(Base):
    __tablename__ = "escuelas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))

    profesores: Mapped[list["Profesor"]] = relationship(
        back_populates="escuela",
        cascade="all, delete-orphan"
    )

    alumnos: Mapped[list["Alumno"]] = relationship(
        back_populates="escuela",
        cascade="all, delete-orphan"
    )

class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    dni: Mapped[str] = mapped_column(String(20), unique=True)
    especialidad: Mapped[str] = mapped_column(String(100))
    escuela_id: Mapped[int] = mapped_column(ForeignKey("escuelas.id"))

    escuela: Mapped["Escuela"] = relationship(back_populates="profesores")

class Alumno(Base):
    __tablename__ = "alumnos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    dni: Mapped[str] = mapped_column(String(20), unique=True)
    curso: Mapped[str] = mapped_column(String(50))
    escuela_id: Mapped[int] = mapped_column(ForeignKey("escuelas.id"))

    escuela: Mapped["Escuela"] = relationship(back_populates="alumnos")

# Creamos la base de datos SQLite
engine = create_engine("sqlite:///escuela.db")

# Creamos las tablas si todavía no existen
Base.metadata.create_all(engine)

# Preparamos las sesiones
Session = sessionmaker(bind=engine)
