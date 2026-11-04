"""
Pruebas unitarias para los Patrones de Comportamiento.
"""

import io
import sys
import unittest
from comportamiento.strategy import (
    DiscountStrategy,
    NoDiscount,
    StudentDiscount,
    EmployeeDiscount,
    VIPDiscount,
    Cart,
)
from comportamiento.observer import (
    Subscriber,
    Channel,
    EmailSubscriber,
    MobileSubscriber,
)
from comportamiento.command import (
    Light,
    Command,
    TurnOnCommand,
    TurnOffCommand,
    RemoteControl,
)
from comportamiento.template_method import Report, TextReport, HTMLReport
from comportamiento.state import (
    OrderState,
    Pending,
    Paid,
    Shipped,
    Delivered,
    Order,
)


class TestComportamiento(unittest.TestCase):
    def test_strategy(self):
        cart = Cart(StudentDiscount())
        cart.add(100)
        cart.add(50)
        self.assertAlmostEqual(cart.total(), 135.0)

        cart.strategy = VIPDiscount()
        self.assertAlmostEqual(cart.total(), 105.0)

        cart.strategy = EmployeeDiscount()
        self.assertAlmostEqual(cart.total(), 120.0)

        cart.strategy = NoDiscount()
        self.assertAlmostEqual(cart.total(), 150.0)

        with self.assertRaises(NotImplementedError):
            DiscountStrategy().apply(100.0)

    def test_observer(self):
        captured_output = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            channel = Channel("DevTalks")
            email_sub = EmailSubscriber("ana@x.com")
            mobile_sub = MobileSubscriber("@carlos")
            channel.subscribe(email_sub)
            channel.subscribe(mobile_sub)
            channel.publish("Patrones de Diseño en Python")

            # Probar desuscripción
            channel.unsubscribe(email_sub)
            channel.publish("Segundo Video")
        finally:
            sys.stdout = old_stdout

        output = captured_output.getvalue()
        self.assertIn("DevTalks publicó: Patrones de Diseño en Python", output)
        self.assertIn(
            "-> Email a ana@x.com: nuevo video 'Patrones de Diseño en Python'",
            output,
        )
        self.assertIn(
            "-> Push a @carlos: 'Patrones de Diseño en Python'", output
        )
        self.assertIn("DevTalks publicó: Segundo Video", output)
        self.assertNotIn("-> Email a ana@x.com: nuevo video 'Segundo Video'", output)

        with self.assertRaises(NotImplementedError):
            Subscriber().update("test")

    def test_command(self):
        light = Light()
        remote = RemoteControl()

        self.assertFalse(light.is_on)
        remote.press(TurnOnCommand(light))
        self.assertTrue(light.is_on)

        remote.press(TurnOffCommand(light))
        self.assertFalse(light.is_on)

        remote.undo()
        self.assertTrue(light.is_on)

        remote.undo()
        self.assertFalse(light.is_on)

        # Undo on empty history does not fail
        remote.undo()
        self.assertFalse(light.is_on)

        with self.assertRaises(NotImplementedError):
            Command().execute()
        with self.assertRaises(NotImplementedError):
            Command().undo()

    def test_template_method(self):
        data = {
            "title": "Ventas Q4",
            "content": "Crecimos 12%",
            "author": "C. Sierra",
        }
        text_rep = TextReport().generate(data)
        html_rep = HTMLReport().generate(data)

        self.assertIn("=== Ventas Q4 ===", text_rep)
        self.assertIn("Crecimos 12%", text_rep)
        self.assertIn("-- Generado por C. Sierra --", text_rep)

        self.assertIn("<h1>Ventas Q4</h1>", html_rep)
        self.assertIn("<p>Crecimos 12%</p>", html_rep)
        self.assertIn("<footer>C. Sierra</footer>", html_rep)

        with self.assertRaises(NotImplementedError):
            Report().header(data)
        with self.assertRaises(NotImplementedError):
            Report().body(data)
        with self.assertRaises(NotImplementedError):
            Report().footer(data)

    def test_state_flow(self):
        captured_output = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            order = Order()
            self.assertIsInstance(order.state, Pending)

            order.ship()  # No permitido
            self.assertIsInstance(order.state, Pending)

            order.pay()
            self.assertIsInstance(order.state, Paid)

            order.pay()  # No permitido en Paid
            self.assertIsInstance(order.state, Paid)

            order.ship()
            self.assertIsInstance(order.state, Shipped)

            order.deliver()
            self.assertIsInstance(order.state, Delivered)

            order.ship()  # No permitido en Delivered
            self.assertIsInstance(order.state, Delivered)
        finally:
            sys.stdout = old_stdout

        output = captured_output.getvalue()
        self.assertIn("Acción no permitida en este estado", output)
        self.assertIn("Pago recibido", output)
        self.assertIn("Pedido enviado", output)
        self.assertIn("Pedido entregado", output)


if __name__ == "__main__":
    unittest.main()
