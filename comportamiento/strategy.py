"""
3.1. Strategy – Algoritmos intercambiables
Problema: una tienda aplica distintos descuentos: cliente normal (0%), estudiante (10%),
empleado (20%) y VIP (30%). Queremos cambiar la regla sin llenar el código de if/elif.
"""


# Estrategias intercambiables
class DiscountStrategy:
    def apply(self, total: float) -> float:
        raise NotImplementedError


class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total


class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.90


class EmployeeDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.80


class VIPDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.70


# Contexto que recibe la estrategia
class Cart:
    def __init__(self, strategy: DiscountStrategy):
        self.items: list[float] = []
        self.strategy = strategy

    def add(self, price: float):
        self.items.append(price)

    def total(self) -> float:
        return self.strategy.apply(sum(self.items))


def run_strategy():
    cart = Cart(StudentDiscount())
    cart.add(100)
    cart.add(50)
    total_student = cart.total()
    print(total_student)  # 135.0

    cart.strategy = VIPDiscount()
    total_vip = cart.total()
    print(total_vip)  # 105.0

    return total_student, total_vip


if __name__ == "__main__":
    run_strategy()
