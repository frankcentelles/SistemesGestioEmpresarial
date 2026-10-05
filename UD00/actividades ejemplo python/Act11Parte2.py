import csv
import hashlib
import os

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class VentanaLogin(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Organizamos los elementos verticalmente
        self.orientation = "vertical"
        # establece el espacio interior
        self.padding = 30
        # separacion entre elemntos
        self.spacing = 15

        # Diccionario que almacenara usuarios y hashes
        self.usuarios = {}

        # Cargamos los usuarios del archivo CSV
        self.cargarUsuarios()

        # Titulo de la interfaz
        self.titulo = Label(
            text="INICIO DE SESION",
            font_size=24
        )
        self.add_widget(self.titulo)

        # Campo para introducir el usuario
        self.campoUsuario = TextInput(
            hint_text="Usuario",
            multiline=False
        )
        self.add_widget(self.campoUsuario)

        # Campo para introducir la contrasena
        self.campoContrasena = TextInput(
            hint_text="Contrasena",
            password=True,
            multiline=False
        )
        self.add_widget(self.campoContrasena)

        # Boton para comprobar los datos
        self.boton = Button(
            text="Comprobar",
            size_hint=(1, 0.5)
        )
        self.boton.bind(on_press=self.comprobarLogin)
        self.add_widget(self.boton)

        # Etiqueta donde mostraremos el resultado
        self.mensaje = Label(text="")
        self.add_widget(self.mensaje)

    def cargarUsuarios(self):
        # Obtenemos la ruta del CSV junto al programa
        ruta = os.path.join(os.path.dirname(__file__), "users.csv")

        # Comprobamos que exista el archivo
        if not os.path.isfile(ruta):
            print("No se encuentra users.csv")
            return

        # Leemos los usuarios del archivo
        with open(ruta, "r", encoding="utf-8", newline="") as fichero:
            lector = csv.DictReader(fichero)

            for fila in lector:
                usuario = fila["usuario"].strip()
                hashContrasena = fila["hash"].strip()

                self.usuarios[usuario] = hashContrasena

    def comprobarLogin(self, boton):
        # Obtenemos los datos de los campos
        usuario = self.campoUsuario.text.strip()
        contrasena = self.campoContrasena.text

        # Calculamos el SHA1 de la contrasena
        hashIntroducido = hashlib.sha1(
            contrasena.encode("utf-8")
        ).hexdigest()

        # Comprobamos si existe el usuario y coincide el hash
        if usuario in self.usuarios:
            if hashIntroducido == self.usuarios[usuario]:
                self.mensaje.text = "OK"
                self.mensaje.color = (0, 0.7, 0, 1)
                return

        # Si los datos no coinciden, mostramos ERROR
        self.mensaje.text = "ERROR"
        self.mensaje.color = (1, 0, 0, 1)

class AplicacionLogin(App):

    def build(self):
        # Devolvemos la interfaz que mostrara Kivy.
        return VentanaLogin()


if __name__ == "__main__":
    AplicacionLogin().run()
