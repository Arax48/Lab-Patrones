# Laboratorio: Patrones de Diseño en Python

**Universidad Nacional de Colombia**  
**Facultad de Ingeniería**  
**Departamento de Ingeniería de Sistemas e Industrial**  
**Asignatura:** Ingeniería de Software II  

---

## 👥 Autores

* **Alejandro Rodríguez Arciniegas**
* **Bryant Antony Rosero Rojas**

### 👨‍🏫 Profesores
* **Ing. Carlos Sierra**
* **Ing. Liliana Olarte**

---

## 🎯 Objetivo del Laboratorio

Desarrollar la capacidad para identificar, comprender e implementar los principales patrones de diseño de software (creacionales, estructurales y de comportamiento) mediante la solución progresiva de problemas reales utilizando Python.

El laboratorio busca aplicar cada patrón de manera práctica, resolviendo necesidades específicas de diseño como la creación flexible de objetos, la organización eficiente de estructuras y la comunicación adecuada entre componentes, con el fin de maximizar la modularidad, reutilización, mantenibilidad y escalabilidad del software.

---

## 📁 Estructura del Proyecto

El proyecto está estructurado modularmente en paquetes según la categoría de cada patrón de diseño:

```text
Lab-Patrones/
├── creacionales/                  # Patrones de creación de objetos
│   ├── __init__.py
│   ├── builder.py                 # 1.1 Builder (Café personalizado)
│   ├── prototype.py               # 1.2 Prototype (Plantillas de promociones)
│   ├── singleton.py               # 1.3 Singleton (Configuración global AppConfig)
│   └── factory_method.py          # 1.4 Factory Method (Fábrica de chocolates Wonka)
├── estructurales/                 # Patrones de composición estructural
│   ├── __init__.py
│   ├── adapter.py                 # 2.1 Adapter (Adaptador de pasarela de pagos)
│   ├── decorator.py               # 2.2 Decorator (Sistema de notificaciones dinámicas)
│   ├── facade.py                  # 2.3 Facade (Fachada Home Theater)
│   └── composite.py               # 2.4 Composite (Jerarquía de archivos y carpetas)
├── comportamiento/                # Patrones de algoritmos y responsabilidades
│   ├── __init__.py
│   ├── strategy.py                # 3.1 Strategy (Estrategias de descuento)
│   ├── observer.py                # 3.2 Observer (Suscripciones a canal de YouTube)
│   ├── command.py                 # 3.3 Command (Control remoto con deshacer)
│   ├── template_method.py         # 3.4 Template Method (Generador de reportes)
│   └── state.py                   # 3.5 State (Gestión de estados de un pedido)
├── tests/                         # Suite de pruebas unitarias exhaustivas
│   ├── __init__.py
│   ├── test_creacionales.py
│   ├── test_estructurales.py
│   └── test_comportamiento.py
├── main.py                        # Script orquestador principal
├── .gitignore
└── README.md                      # Documentación completa del laboratorio
```

---

## 🧠 Patrones de Diseño Implementados

### 1. Patrones Creacionales

#### 1.1 Builder (Construir objetos paso a paso)
* **Problema:** Creación de pedidos de café personalizados con múltiples parámetros opcionales (tamaño, tipo de leche, cucharadas de azúcar, extras) sin recurrir a constructores telescópicos inmanejables.
* **Solución:** `CoffeeBuilder` encapsula paso a paso la configuración de la instancia `Coffee` con una interfaz fluida (`fluent interface`), permitiendo resetear y generar objetos complejos limpiamente.

#### 1.2 Prototype (Clonar objetos)
* **Problema:** Copiar repetidamente plantillas de banners promocionales (`PromoBanner`) para diferentes días u ocasiones modificando únicamente atributos específicos (título o descuento) sin reiniciar la creación desde cero.
* **Solución:** Método `clone()` implementado mediante `copy.deepcopy()`, produciendo copias independientes de la plantilla prototipo original.

#### 1.3 Singleton (Una sola instancia)
* **Problema:** Garantizar que exista una única instancia de configuración centralizada en la aplicación (`AppConfig`), como la URL de la base de datos.
* **Solución:** Sobrescritura de `__new__` controlando la asignación del objeto `_instance` en memoria para asegurar que todas las llamadas retornen siempre la misma referencia.

#### 1.4 Factory Method (Fábrica de objetos)
* **Problema:** Creación desacoplada de diferentes dulces y chocolates Wonka (`ChocolateBar`, `FizzyLiftingDrink`, `EverlastingGobstopper`) según el requerimiento del cliente.
* **Solución:** `WonkaFactory` provee el método `create_candy()` que abstrae la instanciación de las subclases concretas a partir de un identificador en texto.

---

### 2. Patrones Estructurales

#### 2.1 Adapter (Adaptar una interfaz a otra)
* **Problema:** Un nuevo sistema espera interactuar con un método `pay(amount: float)` en dólares, pero el sistema existente de pasarela heredada expone `make_payment(value_in_cents: int)` en centavos.
* **Solución:** `LegacyPaymentAdapter` implementa `PaymentProcessor` y traduce la llamada y unidades matemáticas hacia la interfaz de `LegacyPaymentGateway`.

#### 2.2 Decorator (Añadir funcionalidades dinámicamente)
* **Problema:** Extender dinámicamente un sistema de notificaciones base (`EmailNotifier`) para agregar canales adicionales como `SMSDecorator` y `SlackDecorator` sin generar una explosión combinatoria de subclases.
* **Solución:** Decoradores que envuelven la interfaz común `Notifier`, ejecutando su propia lógica e invocando de forma encadenada a la instancia envuelta.

#### 2.3 Facade (Fachada simple sobre un subsistema complejo)
* **Problema:** La interacción con un sistema de cine en casa requiere coordinar el proyector (`Projector`), el sistema de sonido (`SoundSystem`) y el reproductor de streaming (`StreamingPlayer`).
* **Solución:** `HomeTheaterFacade` ofrece métodos simples y de alto nivel (`ver_pelicula()` y `terminar()`) ocultando la complejidad y orquestación del subsistema.

#### 2.4 Composite (Tratar objetos individuales y grupos de la misma forma)
* **Problema:** Calcular recursivamente el tamaño de una estructura de sistema de archivos compuesta por archivos (`File`) y carpetas anidadas (`Folder`).
* **Solución:** Ambos implementan la clase base `FileSystemItem` con el método común `get_size()`, permitiendo tratar hojas y contenedores de manera uniforme.

---

### 3. Patrones de Comportamiento

#### 3.1 Strategy (Algoritmos intercambiables)
* **Problema:** Aplicar diferentes reglas de descuentos (`NoDiscount`, `StudentDiscount`, `EmployeeDiscount`, `VIPDiscount`) en el carrito de compras (`Cart`) sin usar estructuras anidadas `if/elif`.
* **Solución:** Cada algoritmo de descuento se encapsula en una clase que implementa `DiscountStrategy`, permitiendo al carrito intercambiar la estrategia en tiempo de ejecución.

#### 3.2 Observer (Notificar a varios suscriptores)
* **Problema:** Cuando un canal de YouTube (`Channel`) publica un nuevo contenido, debe notificar automáticamente a múltiples suscriptores (`EmailSubscriber`, `MobileSubscriber`) sin conocer sus detalles de implementación internos.
* **Solución:** Sujeto observable que mantiene una lista dinámica de observadores (`Subscriber`) suscritos, notificándoles ante el evento `publish()`.

#### 3.3 Command (Encapsular una petición como objeto)
* **Problema:** Un control remoto (`RemoteControl`) debe ejecutar órdenes sobre un dispositivo (`Light`), guardar un historial de operaciones y permitir deshacer (`undo`) las acciones ejecutadas.
* **Solución:** Encapsulamiento de las acciones en objetos comando (`TurnOnCommand`, `TurnOffCommand`) que implementan `execute()` y `undo()`.

#### 3.4 Template Method (Esqueleto de un algoritmo)
* **Problema:** Generar reportes en múltiples formatos (texto plano con `TextReport` o HTML con `HTMLReport`), conservando un esqueleto común fijo (encabezado, cuerpo y pie).
* **Solución:** La clase base `Report` define el método plantilla `generate()`, delegando la implementación de los pasos variables a las subclases correspondientes.

#### 3.5 State (Cambiar de comportamiento según el estado interno)
* **Problema:** Manejar el flujo de vida de un pedido en comercio electrónico (`Pending` → `Paid` → `Shipped` → `Delivered`) restringiendo las acciones según el estado activo sin llenar el código de sentencias condicionales.
* **Solución:** Cada estado se modela como una clase derivada de `OrderState`, y el pedido (`Order`) delega sus operaciones (`pay()`, `ship()`, `deliver()`) en su estado actual, permitiendo transiciones válidas.

---

## 🚀 Instrucciones de Ejecución

### Prerrequisitos
* Python 3.8 o superior instalado en el sistema.

### Ejecución de la Demostración General
Para ejecutar todos los patrones de diseño y visualizar las salidas descritas en la guía del laboratorio:

```bash
python3 main.py
```

### Ejecución Individual de Módulos
Cada patrón puede ser ejecutado de forma aislada:

```bash
# Patrones Creacionales
python3 creacionales/builder.py
python3 creacionales/prototype.py
python3 creacionales/singleton.py
python3 creacionales/factory_method.py

# Patrones Estructurales
python3 estructurales/adapter.py
python3 estructurales/decorator.py
python3 estructurales/facade.py
python3 estructurales/composite.py

# Patrones de Comportamiento
python3 comportamiento/strategy.py
python3 comportamiento/observer.py
python3 comportamiento/command.py
python3 comportamiento/template_method.py
python3 comportamiento/state.py
```

---

## 🧪 Ejecución de Pruebas Unitarias

El proyecto cuenta con una batería completa de pruebas unitarias automatizadas (`unittest`) que verifican el 100% de la funcionalidad de cada patrón:

```bash
python3 -m unittest discover tests -v
```
