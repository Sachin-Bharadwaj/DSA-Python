
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def forward_traversal(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

    def reverse_traversal(self):
        if self.head is None:
            print("List is empty")
        else:
            # first reach the last node using the head
            current = self.head
            while current.next is not None:
                current = current.next
            # now current is the last node, start reverse traversal
            while current is not None:
                print(current.data, end=" -> ")
                current = current.prev
            print("None")

    def insertion_at_begining(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head.prev = nb
        self.head = nb

    def insert_at_end(self, data):
        ne = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = ne
        ne.prev = current

    def insert_at_specified(self, data, pos):
        if pos==0:
            self.insertion_at_begining(data)
        else:
            nib = Node(data)
            current = self.head
            for i in range(pos):
                current = current.next
            nib.prev = current.prev
            current.prev.next = nib
            current.prev = nib
            nib.next = current

    def deletion_at_begining(self):
        self.head = self.head.next
        self.head.prev = None

    def deletion_at_end(self):
        current = self.head
        # traverse to the end
        while current.next is not None:
            current = current.next
        current.prev.next = None
        current.prev = None

    def deletion_at_specified(self, pos):
        if pos==0:
            self.deletion_at_begining()
        else:
            current = self.head
            for i in range(pos):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            current.next = None
            current.prev = None

            
if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.prev = n4
    n4.prev = n3
    n3.prev = n2
    n2.prev = n1

    dll = DoublyLinkedList()
    dll.head = n1
    print("forward traversal")
    dll.forward_traversal()
    print("reverse traversal")
    dll.reverse_traversal()
    print("insert at begining")
    dll.insertion_at_begining(-100)
    dll.forward_traversal()
    print("insert at end")
    dll.insert_at_end(-200)
    dll.forward_traversal()
    print("insert at specified")
    dll.insert_at_specified(1000, 1)
    dll.forward_traversal()
    print("deletion at begining")
    dll.deletion_at_begining()
    dll.forward_traversal()
    print("deletion at end")
    dll.deletion_at_end()
    dll.forward_traversal()
    print("deletion at specified")
    dll.deletion_at_specified(1)
    dll.forward_traversal()