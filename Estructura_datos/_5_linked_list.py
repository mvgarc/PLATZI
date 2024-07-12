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