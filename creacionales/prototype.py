"""
1.2. Prototype – Clonar objetos
Problema: tenemos una plantilla de promoción y queremos copiarla varias veces y luego cambiar pequeños detalles.
"""

import copy


class PromoBanner:
    def __init__(self, title: str, text: str, discount: int):
        self.title = title
        self.text = text
        self.discount = discount

    def clone(self) -> "PromoBanner":
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"[{self.title}] {self.text} ({self.discount}% off)"


def run_prototype():
    base_promo = PromoBanner(
        title="Promo de la semana",
        text="Café + croissant",
        discount=20,
    )
    promo_lunes = base_promo.clone()
    promo_lunes.title = "Lunes de energía"

    promo_viernes = base_promo.clone()
    promo_viernes.discount = 30

    print(base_promo)
    print(promo_lunes)
    print(promo_viernes)
    return base_promo, promo_lunes, promo_viernes


if __name__ == "__main__":
    run_prototype()
