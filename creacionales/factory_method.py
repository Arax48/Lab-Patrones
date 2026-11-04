"""
1.4. Factory Method – Fábrica de objetos
Problema: queremos crear distintos tipos de chocolates. Tú solo haces el pedido y la fábrica te
entrega el chocolate correcto.
"""


class Chocolate:
    def prepare(self) -> str:
        raise NotImplementedError


class ChocolateBar(Chocolate):
    def prepare(self) -> str:
        return "Preparando una barra de chocolate Wonka"


class FizzyLiftingDrink(Chocolate):
    def prepare(self) -> str:
        return "Preparando un Fizzy Lifting Drink (bebida burbujeante)"


class EverlastingGobstopper(Chocolate):
    def prepare(self) -> str:
        return "Preparando un Everlasting Gobstopper (caramelo eterno)"


class WonkaFactory:
    def create_candy(self, candy_type: str) -> Chocolate:
        candy_type = candy_type.lower()
        if candy_type == "bar":
            return ChocolateBar()
        elif candy_type == "fizzy":
            return FizzyLiftingDrink()
        elif candy_type == "gobstopper":
            return EverlastingGobstopper()
        else:
            raise ValueError("Ese dulce no existe en la fábrica de Willy Wonka.")


def run_factory():
    factory = WonkaFactory()
    r1 = factory.create_candy("bar").prepare()
    r2 = factory.create_candy("fizzy").prepare()
    r3 = factory.create_candy("gobstopper").prepare()
    print(r1)
    print(r2)
    print(r3)
    return r1, r2, r3


if __name__ == "__main__":
    run_factory()
