"""
2.1. Adapter – Adaptar una interfaz a otra
Problema: tenemos un sistema nuevo que espera un método pay(amount), pero la pasarela de
pagos antigua expone make_payment(value_in_cents). Queremos reutilizar la pasarela vieja sin
modificarla.
"""


# Interfaz que espera nuestra aplicación nueva
class PaymentProcessor:
    def pay(self, amount: float) -> str:
        raise NotImplementedError


# Sistema legacy (no lo podemos cambiar)
class LegacyPaymentGateway:
    def make_payment(self, value_in_cents: int) -> str:
        return f"Pago legacy procesado por {value_in_cents} centavos"


# Adapter
class LegacyPaymentAdapter(PaymentProcessor):
    def __init__(self, legacy_gateway: LegacyPaymentGateway):
        self.legacy = legacy_gateway

    def pay(self, amount: float) -> str:
        # Adapta la unidad (dólares -> centavos) y el nombre del método
        cents = int(amount * 100)
        return self.legacy.make_payment(cents)


def run_adapter():
    gateway = LegacyPaymentGateway()
    processor = LegacyPaymentAdapter(gateway)
    res = processor.pay(25.50)
    print(res)  # Pago legacy procesado por 2550 centavos
    return res


if __name__ == "__main__":
    run_adapter()
