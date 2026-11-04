"""
3.4. Template Method – Esqueleto de un algoritmo
Problema: queremos generar reportes en distintos formatos (texto plano, HTML). Los pasos son
siempre los mismos (encabezado, cuerpo, pie) pero el formato cambia. Queremos fijar el orden
y dejar que las subclases personalicen cada paso.
"""


# Clase base con el algoritmo completo
class Report:
    # Template method: define el orden, no se sobreescribe
    def generate(self, data: dict) -> str:
        parts = [self.header(data), self.body(data), self.footer(data)]
        return "\n".join(parts)

    def header(self, data: dict) -> str:
        raise NotImplementedError

    def body(self, data: dict) -> str:
        raise NotImplementedError

    def footer(self, data: dict) -> str:
        raise NotImplementedError


# Subclases que rellenan los “huecos”:
class TextReport(Report):
    def header(self, data: dict) -> str:
        return f"=== {data['title']} ==="

    def body(self, data: dict) -> str:
        return data["content"]

    def footer(self, data: dict) -> str:
        return f"-- Generado por {data['author']} --"


class HTMLReport(Report):
    def header(self, data: dict) -> str:
        return f"<h1>{data['title']}</h1>"

    def body(self, data: dict) -> str:
        return f"<p>{data['content']}</p>"

    def footer(self, data: dict) -> str:
        return f"<footer>{data['author']}</footer>"


def run_template_method():
    data = {
        "title": "Ventas Q4",
        "content": "Crecimos 12%",
        "author": "C. Sierra",
    }
    text_rep = TextReport().generate(data)
    html_rep = HTMLReport().generate(data)
    print(text_rep)
    print()
    print(html_rep)
    return text_rep, html_rep


if __name__ == "__main__":
    run_template_method()
