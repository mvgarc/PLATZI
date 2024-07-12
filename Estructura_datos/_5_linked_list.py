from _4_nodo import Nodo

class SinglyLinkedList:
    def __init__(self):
        self.tail=None
        self.size= 0

    def append(self, data):
        node = Nodo(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail

            while current.next:
                current=current.next
            
            current.next = node

        self.size+=1

    def size(self):
        return str(self.size)
    
    def iter(self):
        current= self.tail

        while current:
            value= current.data
            current = current.next
            yield value

    def delete(self, data):
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
            else:
                previous.next = current.next
                self.size -=1
                return current.data
            
        previous = current
        current = current.next

    def search(self, data):
        for nodo in self.iter():
            if data == nodo:
                print(f"Data {data} found!")
            else:
                print(f"Data {data} not found!")
                break

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

words = SinglyLinkedList()
words.append ("manzana")
words.append ("pera")
words.append ("durazno")
words.append ("guayaba")
current = words.tail

while current:
    print (current.data)
    current = current.next

#Buscar una palabra
words.search ("miel")