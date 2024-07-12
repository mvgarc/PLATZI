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

probe = head
target_item = 3
new_item = "Z"
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    probe.data = new_item
    print(f"{new_item} replaced the old value in the node number {target_item}")
else:
    print(f"The target item {target_item} is not in the linked list")


head = Nodo("F", head)


new_nodo = Nodo("K")

if head is None:
    head = new_nodo
else:
    probe = head
    while probe.next != None:
        probe = probe.next

    probe.next = new_nodo


removed_item = head.data
head = head.next
print(removed_item)


removed_item = head.data

if head.next is None:
    head = None
else:
    probe = head

    while probe.next.next != None:
        probe = probe.next

    removed_item = probe.next.data
    probe.next = None

print(removed_item)


new_item = input("Enter the new item: ")
index = int(input("Enter the position to inser the new item: "))
if head is None or index < 0:
    head = Nodo("Py", head)
else:
    probe = head

    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1

    probe.next = Nodo(new_item, probe.next)

index = 3

if index <= 0 or head.next is None:
    removed_item = head.data
    head = head.next
    print(removed_item)
else:
    probe = head

    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1

    removed_item = probe.next.data
    probe.next = probe.next.next
    print(removed_item)