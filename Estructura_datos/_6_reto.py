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

        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = new_nodo
    
    def print_list(self):
        actual = self.head
        while actual is not None:
            print (actual.value, end="->")
            actual = actual.next
        print ("None")

array = [1,4,7,8,12]

list_enlazada= ListaEnlazada()
for value in array:
    list_enlazada.agregar(value)
list_enlazada.print_list()