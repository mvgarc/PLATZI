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

probe = head
while probe!= None:
    print (probe.data)
    probe = probe.next

probe = head
target_item = 2
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    print(f"Target item {target_item} has been found")
else:
    print(f"Target item {target_item} is not in the linked list")