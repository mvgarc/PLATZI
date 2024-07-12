from _4_nodo import Nodo

head = None
for count in range (1,6):
    head = Nodo(count, head)

while head!= None:
    print (head.data)
    head = head.next