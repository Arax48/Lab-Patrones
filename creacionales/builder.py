"""
1.1. Builder – Construir objetos paso a paso
Problema: queremos crear cafés personalizados (tamaño, leche, azúcar, extras). Muchos parámetros.
"""


class Coffee:
    def __init__(self, size=None, milk=None, sugar=0, extras=None):
        self.size = size
        self.milk = milk
        self.sugar = sugar
        self.extras = extras or []

    def __str__(self):
        return f"Coffee(size={self.size}, milk={self.milk}, sugar={self.sugar}, extras={self.extras})"


class CoffeeBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._size = None
        self._milk = None
        self._sugar = 0
        self._extras = []
        return self

    def set_size(self, size):
        self._size = size
        return self

    def add_milk(self, milk_type):
        self._milk = milk_type
        return self

    def add_sugar(self, spoons):
        self._sugar = spoons
        return self

    def add_extra(self, extra):
        self._extras.append(extra)
        return self

    def build(self):
        coffee = Coffee(self._size, self._milk, self._sugar, self._extras)
        self.reset()
        return coffee


def run_builder():
    builder = CoffeeBuilder()
    latte = (
        builder.set_size("grande")
        .add_milk("almendra")
        .add_sugar(2)
        .add_extra("canela")
        .build()
    )
    espresso = builder.set_size("pequeño").build()
    print(latte)
    print(espresso)
    return latte, espresso


if __name__ == "__main__":
    run_builder()
