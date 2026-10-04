import requests


def buscarPersonajes(especie):
    # Direccion de la API de personajes
    url = "https://rickandmortyapi.com/api/character/"

    # Parametros que se enviaran a la API
    # se almacenan en un diccionario
    parametros = {
        "species": especie,
        "page": 1
    }

    # Contador de personajes encontrados
    total = 0

    try:
        # Solicitamos los personajes a la API
        # realiza una peticion get
        respuesta = requests.get(
            url,
            # añade los parametros de busqueda
            params=parametros,
            # establece un limite de espera de diez segundos
            timeout=10
        )

        # Comprobamos que la peticion haya sido correcta
        # genera un error si el servidor devuelve un codigo HTTP de error
        respuesta.raise_for_status()

        # Convertimos la respuesta JSON a un diccionario
        datos = respuesta.json()

        # Comprobamos si existen resultados.
        if datos["info"]["count"] == 0:
            print("No se han encontrado personajes.")
            return

        # Leemos todas las paginas de resultados
        while True:

            # Recorremos los personajes de esta pagina
            for personaje in datos["results"]:
                print("Nombre:", personaje["name"])
                print("Especie:", personaje["species"])
                print("Estado:", personaje["status"])
                print("--------------------")
                total += 1

            # Comprobamos si hay una pagina siguiente
            siguiente = datos["info"]["next"]

            if siguiente is None:
                break

            # Solicitamos la pagina siguiente
            respuesta = requests.get(siguiente, timeout=10)
            respuesta.raise_for_status()
            datos = respuesta.json()

        print("Total de personajes:", total)

    except requests.exceptions.Timeout:
        print("Error: la peticion ha tardado demasiado.")

    except requests.exceptions.ConnectionError:
        print("Error: no se ha podido conectar con la API.")

    except requests.exceptions.HTTPError as error:
        print("Error HTTP:", error)

    except requests.exceptions.RequestException as error:
        print("Error en la peticion:", error)


if __name__ == "__main__":
    especie = input("Introduce una especie: ").strip()

    if especie == "":
        print("Debes introducir una especie.")
    else:
        buscarPersonajes(especie)

