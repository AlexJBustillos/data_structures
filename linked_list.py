class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_value = None

class LinkedList:
    def __init__(self):
        self.head = None

list_a = LinkedList()
list_a.head = Node('A')
list_b = Node('B')
list_c = Node('C')

list_a.head.next_value = list_b
list_b.next_value = list_c