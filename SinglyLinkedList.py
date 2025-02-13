
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        if self.head is None:
            print("List is empty")         
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next     
            print("None")

    def insert_at_begining(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_at_end(self, data):
        ne = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = ne

    def insert_at_sepcified_node(self, pos, data):
        if pos == 0:
            self.insert_at_begining(data)
        
        nib = Node(data)
        current = self.head
        for i in range(pos-1):
            current = current.next
        nib.next = current.next
        current.next = nib

    def deletion_at_begining(self):
        a = self.head
        self.head = a.next
        a.next = None

    def deletion_at_end(self):
        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None

    def deletion_at_specified(self, pos):
        if pos == 0:
            self.deletion_at_begining()
        else:
            current = self.head
            prev = None
            for i in range(pos):
                prev = current
                current = current.next
            prev.next = current.next
            current.next = None
    
if __name__ == "__main__":
    sll = SinglyLinkedList()
    n1 = Node(10)
    n2 = Node(20)
    n1.next = n2
    n3 = Node(30)
    n2.next = n3
    n4 = Node(40)
    n3.next = n4

    sll.head = n1
    sll.traversal()
    sll.insert_at_sepcified_node(4, 100)
    sll.traversal()
    sll.deletion_at_begining()
    sll.traversal()
    sll.deletion_at_end()
    sll.traversal()
    sll.deletion_at_specified(2)
    sll.traversal()