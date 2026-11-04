"""
2.4. Composite – Tratar objetos individuales y grupos de la misma forma
Problema: queremos calcular el tamaño total de una carpeta del sistema de archivos. Una
carpeta puede contener archivos y otras carpetas, recursivamente.
"""


# Componente común (hojas y compuestos comparten interfaz)
class FileSystemItem:
    def __init__(self, name: str):
        self.name = name

    def get_size(self) -> int:
        raise NotImplementedError


# Hoja (File) y Compuesto (Folder)
class File(FileSystemItem):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self._size = size

    def get_size(self) -> int:
        return self._size


class Folder(FileSystemItem):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: list[FileSystemItem] = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children)


def run_composite():
    root = Folder("proyecto")
    root.add(File("README.md", 2))
    src = Folder("src")
    src.add(File("main.py", 10))
    src.add(File("utils.py", 5))
    root.add(src)
    total_size = root.get_size()
    print(total_size)  # 17 (se trata igual un archivo que una carpeta)
    return total_size


if __name__ == "__main__":
    run_composite()
