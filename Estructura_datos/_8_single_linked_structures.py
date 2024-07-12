class Nodo():
    def __init__(self, data,next=None):
        self.data= data
        self.next= next

head = None
for count in range (1,6):
    head = Nodo(count, head)

while head!= None:
    print (head.data)
    head = head.next