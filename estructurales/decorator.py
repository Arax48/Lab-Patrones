"""
2.2. Decorator – Añadir funcionalidades dinámicamente
Problema: tenemos un sistema de notificaciones. A veces solo queremos enviar correo, a veces
correo + SMS, a veces correo + SMS + Slack. No queremos crear una clase distinta por cada
combinación.
"""


class Notifier:
    def send(self, message: str) -> None:
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[Email] {message}")


# Decoradores que envuelven a otro Notifier
class NotifierDecorator(Notifier):
    def __init__(self, wrapped: Notifier):
        self._wrapped = wrapped

    def send(self, message: str) -> None:
        self._wrapped.send(message)


class SMSDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"[SMS] {message}")


class SlackDecorator(NotifierDecorator):
    def send(self, message: str) -> None:
        super().send(message)
        print(f"[Slack] {message}")


def run_decorator():
    notifier = SlackDecorator(SMSDecorator(EmailNotifier()))
    notifier.send("Servidor caído")
    return notifier


if __name__ == "__main__":
    run_decorator()
