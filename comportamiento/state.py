"""
3.5. State – Cambiar de comportamiento según el estado interno
Problema: un pedido en un e-commerce pasa por estados: Pendiente → Pagado → Enviado → Entregado.
Las acciones permitidas dependen del estado actual. Queremos evitar un if gigantesco.
"""


# Una clase por estado
class OrderState:
    def pay(self, order: "Order"):
        print("Acción no permitida en este estado")

    def ship(self, order: "Order"):
        print("Acción no permitida en este estado")

    def deliver(self, order: "Order"):
        print("Acción no permitida en este estado")


class Pending(OrderState):
    def pay(self, order: "Order"):
        print("Pago recibido")
        order.state = Paid()


class Paid(OrderState):
    def ship(self, order: "Order"):
        print("Pedido enviado")
        order.state = Shipped()


class Shipped(OrderState):
    def deliver(self, order: "Order"):
        print("Pedido entregado")
        order.state = Delivered()


class Delivered(OrderState):
    pass  # estado final


# Contexto que delega en el estado
class Order:
    def __init__(self):
        self.state: OrderState = Pending()

    def pay(self):
        self.state.pay(self)

    def ship(self):
        self.state.ship(self)

    def deliver(self):
        self.state.deliver(self)


def run_state():
    order = Order()
    order.ship()  # Acción no permitida en este estado (aún está Pending)
    order.pay()  # Pago recibido
    order.ship()  # Pedido enviado
    order.deliver()  # Pedido entregado
    return order


if __name__ == "__main__":
    run_state()
