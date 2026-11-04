"""
3.3. Command – Encapsular una petición como objeto
Problema: un control remoto debe poder ejecutar acciones (prender luz, apagar luz) y además
poder deshacer la última acción. Necesitamos representar cada acción como algo manipulable.
"""


# Receptor y comandos
class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Luz: ON")

    def turn_off(self):
        self.is_on = False
        print("Luz: OFF")


class Command:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError


class TurnOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()


class TurnOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()


# Invocador (el control remoto) con historial
class RemoteControl:
    def __init__(self):
        self.history: list[Command] = []

    def press(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            self.history.pop().undo()


def run_command():
    light = Light()
    remote = RemoteControl()
    remote.press(TurnOnCommand(light))  # Luz: ON
    remote.press(TurnOffCommand(light))  # Luz: OFF
    remote.undo()  # Luz: ON
    remote.undo()  # Luz: OFF
    return light, remote


if __name__ == "__main__":
    run_command()
