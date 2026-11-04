"""
Pruebas unitarias para los Patrones Creacionales.
"""

import unittest
from creacionales.builder import Coffee, CoffeeBuilder
from creacionales.prototype import PromoBanner
from creacionales.singleton import AppConfig
from creacionales.factory_method import (
    Chocolate,
    ChocolateBar,
    FizzyLiftingDrink,
    EverlastingGobstopper,
    WonkaFactory,
)


class TestCreacionales(unittest.TestCase):
    def test_builder_latte(self):
        builder = CoffeeBuilder()
        latte = (
            builder.set_size("grande")
            .add_milk("almendra")
            .add_sugar(2)
            .add_extra("canela")
            .build()
        )
        self.assertEqual(latte.size, "grande")
        self.assertEqual(latte.milk, "almendra")
        self.assertEqual(latte.sugar, 2)
        self.assertIn("canela", latte.extras)
        self.assertIn("Coffee(", str(latte))

    def test_builder_reset_after_build(self):
        builder = CoffeeBuilder()
        espresso = builder.set_size("pequeño").build()
        self.assertEqual(espresso.size, "pequeño")
        self.assertIsNone(espresso.milk)
        self.assertEqual(espresso.sugar, 0)
        self.assertEqual(espresso.extras, [])

    def test_prototype_cloning(self):
        base_promo = PromoBanner(
            title="Promo de la semana",
            text="Café + croissant",
            discount=20,
        )
        promo_lunes = base_promo.clone()
        promo_lunes.title = "Lunes de energía"
        promo_viernes = base_promo.clone()
        promo_viernes.discount = 30

        self.assertEqual(base_promo.title, "Promo de la semana")
        self.assertEqual(base_promo.discount, 20)
        self.assertEqual(promo_lunes.title, "Lunes de energía")
        self.assertEqual(promo_lunes.discount, 20)
        self.assertEqual(promo_viernes.title, "Promo de la semana")
        self.assertEqual(promo_viernes.discount, 30)
        self.assertEqual(
            str(promo_lunes),
            "[Lunes de energía] Café + croissant (20% off)",
        )

    def test_singleton_single_instance(self):
        config1 = AppConfig("postgres://prod")
        config2 = AppConfig("otro")
        self.assertIs(config1, config2)
        self.assertEqual(config1.db_url, "postgres://prod")
        self.assertEqual(config2.db_url, "postgres://prod")

    def test_factory_method(self):
        factory = WonkaFactory()
        candy_bar = factory.create_candy("bar")
        candy_fizzy = factory.create_candy("fizzy")
        candy_gobstopper = factory.create_candy("gobstopper")

        self.assertIsInstance(candy_bar, ChocolateBar)
        self.assertIsInstance(candy_fizzy, FizzyLiftingDrink)
        self.assertIsInstance(candy_gobstopper, EverlastingGobstopper)

        self.assertEqual(
            candy_bar.prepare(), "Preparando una barra de chocolate Wonka"
        )
        self.assertEqual(
            candy_fizzy.prepare(),
            "Preparando un Fizzy Lifting Drink (bebida burbujeante)",
        )
        self.assertEqual(
            candy_gobstopper.prepare(),
            "Preparando un Everlasting Gobstopper (caramelo eterno)",
        )

        with self.assertRaises(ValueError):
            factory.create_candy("invalid_candy")

        with self.assertRaises(NotImplementedError):
            Chocolate().prepare()


if __name__ == "__main__":
    unittest.main()
