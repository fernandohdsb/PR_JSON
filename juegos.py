import json
datos = json.load(open("jugos.json"))


def gta():
    personajes = ["Franklin","Trevor","Michael"]

    while True:
        personaje= input("Elige un personaje de gta v (Franklin,Trevor,Michael): ")
        if personaje in personajes: break


    print(f"El personaje {personaje} tiene una dificultad {datos["videojuegos"][1]["dificultad"][personaje]}")




def disponibilidad():
    juegos = ["The legend of zelda", "GTA V", "Minecraft","Mario bros","Uncharted"]
    codigoJuego = {
        "The legend of zelda":0, "GTA V":1, "Minecraft":2,"Mario bros":3,"Uncharted":4
    }
    while True:
        juego = input("Nombre del juego(The legend of zelda, GTA V, Minecraft, Mario bros, Uncharted): ")
        if juego in juegos: break

    print(f"El juego {juego}  tiene {datos["videojuegos"][codigoJuego[juego]]["ejemplares_disponibles"]} disponibles")

disponibilidad()