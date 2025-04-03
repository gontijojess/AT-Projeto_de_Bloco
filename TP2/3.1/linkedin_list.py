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