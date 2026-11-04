"""
3.2. Observer – Notificar a varios suscriptores
Problema: cuando un canal de YouTube publica un video, todos sus suscriptores deben enterarse.
El canal no debería conocer a cada suscriptor por nombre.
"""


# Sujeto (observable) y observador
class Subscriber:
    def update(self, video: str):
        raise NotImplementedError


class Channel:
    def __init__(self, name: str):
        self.name = name
        self._subs: list[Subscriber] = []

    def subscribe(self, sub: Subscriber):
        self._subs.append(sub)

    def unsubscribe(self, sub: Subscriber):
        self._subs.remove(sub)

    def publish(self, video: str):
        print(f"\n{self.name} publicó: {video}")
        for sub in self._subs:
            sub.update(video)


# Suscriptores concretos
class EmailSubscriber(Subscriber):
    def __init__(self, email: str):
        self.email = email

    def update(self, video: str):
        print(f" -> Email a {self.email}: nuevo video '{video}'")


class MobileSubscriber(Subscriber):
    def __init__(self, user: str):
        self.user = user

    def update(self, video: str):
        print(f" -> Push a {self.user}: '{video}'")


def run_observer():
    channel = Channel("DevTalks")
    channel.subscribe(EmailSubscriber("ana@x.com"))
    channel.subscribe(MobileSubscriber("@carlos"))
    channel.publish("Patrones de Diseño en Python")
    return channel


if __name__ == "__main__":
    run_observer()
