class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, value):
        new_nodo = Nodo(value)
        if self.head is None:
            self.head = new_nodo