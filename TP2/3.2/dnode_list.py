class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, key):
        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        if not current:
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.head
        if not current:
            print("None")
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

print("=== Singly Linked List ===")
linked_list = LinkedList()
linked_list.insert_at_beginning(15)
linked_list.insert_at_beginning(25)
linked_list.insert_at_beginning(33)
linked_list.insert_at_beginning(47)
linked_list.insert_at_end(55)
linked_list.insert_at_end(62)
linked_list.insert_at_beginning(5)

print("Lista após inserções:")
linked_list.traverse()

linked_list.remove(15)
print("Lista após remoção do 15:")
linked_list.traverse()

linked_list.remove(55)
print("Lista após remoção do 55:")
linked_list.traverse()

print("\n=== Doubly Linked List ===")
dll = DoublyLinkedList()
dll.insert_at_beginning(12)
dll.insert_at_beginning(24)
dll.insert_at_end(37)
dll.insert_at_end(49)
dll.insert_at_beginning(2)

print("Lista percorrendo da frente para trás:")
dll.traverse_forward()

print("Lista percorrendo de trás para frente:")
dll.traverse_backward()

dll.remove(24)
print("Lista percorrendo da frente para trás após remoção de 24:")
dll.traverse_forward()