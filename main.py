"""
Laboratorio – Patrones de Diseño
Ingeniería de Software II
Universidad Nacional de Colombia

Autores:
- Alejandro Rodríguez Arciniegas
- Bryant Antony Rosero Rojas

Profesores:
- Ing. Carlos Sierra
- Ing. Liliana Olarte
"""

from creacionales.builder import run_builder
from creacionales.prototype import run_prototype
from creacionales.singleton import run_singleton
from creacionales.factory_method import run_factory

from estructurales.adapter import run_adapter
from estructurales.decorator import run_decorator
from estructurales.facade import run_facade
from estructurales.composite import run_composite

from comportamiento.strategy import run_strategy
from comportamiento.observer import run_observer
from comportamiento.command import run_command
from comportamiento.template_method import run_template_method
from comportamiento.state import run_state


def main():
    print("=" * 70)
    print(" LABORATORIO: PATRONES DE DISEÑO - INGENIERÍA DE SOFTWARE II")
    print(" Autores: Alejandro Rodríguez Arciniegas, Bryant Antony Rosero Rojas")
    print("=" * 70)

    # 1. Patrones Creacionales
    print("\n" + "#" * 60)
    print(" 1. PATRONES CREACIONALES")
    print("#" * 60)

    print("\n--- 1.1 Builder ---")
    run_builder()

    print("\n--- 1.2 Prototype ---")
    run_prototype()

    print("\n--- 1.3 Singleton ---")
    run_singleton()

    print("\n--- 1.4 Factory Method ---")
    run_factory()

    # 2. Patrones Estructurales
    print("\n" + "#" * 60)
    print(" 2. PATRONES ESTRUCTURALES")
    print("#" * 60)

    print("\n--- 2.1 Adapter ---")
    run_adapter()

    print("\n--- 2.2 Decorator ---")
    run_decorator()

    print("\n--- 2.3 Facade ---")
    run_facade()

    print("\n--- 2.4 Composite ---")
    run_composite()

    # 3. Patrones de Comportamiento
    print("\n" + "#" * 60)
    print(" 3. PATRONES DE COMPORTAMIENTO")
    print("#" * 60)

    print("\n--- 3.1 Strategy ---")
    run_strategy()

    print("\n--- 3.2 Observer ---")
    run_observer()

    print("\n--- 3.3 Command ---")
    run_command()

    print("\n--- 3.4 Template Method ---")
    run_template_method()

    print("\n--- 3.5 State ---")
    run_state()

    print("\n" + "=" * 70)
    print(" ¡Todos los patrones se han ejecutado con éxito!")
    print("=" * 70)


if __name__ == "__main__":
    main()
