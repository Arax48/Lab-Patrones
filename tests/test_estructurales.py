"""
Pruebas unitarias para los Patrones Estructurales.
"""

import io
import sys
import unittest
from estructurales.adapter import (
    PaymentProcessor,
    LegacyPaymentGateway,
    LegacyPaymentAdapter,
)
from estructurales.decorator import (
    Notifier,
    EmailNotifier,
    SMSDecorator,
    SlackDecorator,
)
from estructurales.facade import (
    Projector,
    SoundSystem,
    StreamingPlayer,
    HomeTheaterFacade,
)
from estructurales.composite import FileSystemItem, File, Folder


class TestEstructurales(unittest.TestCase):
    def test_adapter(self):
        legacy = LegacyPaymentGateway()
        adapter = LegacyPaymentAdapter(legacy)
        result = adapter.pay(25.50)
        self.assertEqual(result, "Pago legacy procesado por 2550 centavos")

        with self.assertRaises(NotImplementedError):
            PaymentProcessor().pay(10.0)

    def test_decorator(self):
        captured_output = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            notifier = SlackDecorator(SMSDecorator(EmailNotifier()))
            notifier.send("Alerta de prueba")
        finally:
            sys.stdout = old_stdout

        output = captured_output.getvalue()
        self.assertIn("[Email] Alerta de prueba", output)
        self.assertIn("[SMS] Alerta de prueba", output)
        self.assertIn("[Slack] Alerta de prueba", output)

        with self.assertRaises(NotImplementedError):
            Notifier().send("Test")

    def test_facade(self):
        captured_output = io.StringIO()
        old_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            facade = HomeTheaterFacade(
                Projector(), SoundSystem(), StreamingPlayer()
            )
            facade.ver_pelicula("Interstellar")
            facade.terminar()
        finally:
            sys.stdout = old_stdout

        output = captured_output.getvalue()
        self.assertIn("Proyector encendido", output)
        self.assertIn("Volumen en 7", output)
        self.assertIn("Reproduciendo 'Interstellar'", output)
        self.assertIn("Reproducción detenida", output)
        self.assertIn("Sonido apagado", output)
        self.assertIn("Proyector apagado", output)

    def test_composite(self):
        root = Folder("proyecto")
        root.add(File("README.md", 2))
        src = Folder("src")
        src.add(File("main.py", 10))
        src.add(File("utils.py", 5))
        root.add(src)

        self.assertEqual(root.get_size(), 17)
        self.assertEqual(src.get_size(), 15)

        with self.assertRaises(NotImplementedError):
            FileSystemItem("item").get_size()


if __name__ == "__main__":
    unittest.main()
