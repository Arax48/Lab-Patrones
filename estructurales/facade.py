"""
2.3. Facade – Una fachada simple sobre un subsistema complejo
Problema: para ver una película en casa hay que prender el proyector, bajar la pantalla,
encender el sonido y poner el reproductor. Queremos un solo botón: ver_pelicula().
"""


# El subsistema (varias clases independientes)
class Projector:
    def on(self):
        print("Proyector encendido")

    def off(self):
        print("Proyector apagado")


class SoundSystem:
    def set_volume(self, level: int):
        print(f"Volumen en {level}")

    def off(self):
        print("Sonido apagado")


class StreamingPlayer:
    def play(self, movie: str):
        print(f"Reproduciendo '{movie}'")

    def stop(self):
        print("Reproducción detenida")


# La fachada que lo orquesta todo
class HomeTheaterFacade:
    def __init__(
        self,
        projector: Projector,
        sound: SoundSystem,
        player: StreamingPlayer,
    ):
        self.projector = projector
        self.sound = sound
        self.player = player

    def ver_pelicula(self, movie: str):
        self.projector.on()
        self.sound.set_volume(7)
        self.player.play(movie)

    def terminar(self):
        self.player.stop()
        self.sound.off()
        self.projector.off()


def run_facade():
    theater = HomeTheaterFacade(Projector(), SoundSystem(), StreamingPlayer())
    theater.ver_pelicula("Interstellar")
    theater.terminar()
    return theater


if __name__ == "__main__":
    run_facade()
