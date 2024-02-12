# basic linked list implimentation
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
# different operations on linkedlist
class Operations:
    def __init__(self,head):
        self.head = head
        
    def toArray(self):
        arr = []
        curr = self.head
        while curr.next !=None:
            arr.append(curr.value)
            curr = curr.next
        arr.append(curr.value)
        return arr
a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
d = Operations(a)
d.toArray()


    
