class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_dnode = DNode(data)
        if self.head is not None:
            self.head.prev = new_dnode
        new_dnode.next = self.head
        self.head = new_dnode

    def insert_at_end(self, data):
        new_dnode = DNode(data)
        if self.head is None:
            self.head = new_dnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_dnode
        new_dnode.prev = current

    def remove(self, key):
        current = self.head
        while current and current.data != key:
            current = current.next
        if current is None:
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

    def sort_insertion_sort(self):
        if not self.head or not self.head.next:
            return
        current = self.head.next
        while current:
            key = current
            while key.prev and key.data < key.prev.data:
                key.data, key.prev.data = key.prev.data, key.data
                key = key.prev
            current = current.next

    def merge(self, new_list):
        merged_list = DoublyLinkedList()
        first = self.head
        second = new_list.head

        while first and second:
            if first.data <= second.data:
                merged_list.insert_at_end(first.data)
                first = first.next
            else:
                merged_list.insert_at_end(second.data)
                second = second.next
        
        while first:
            merged_list.insert_at_end(first.data)
            first = first.next
        
        while second:
            merged_list.insert_at_end(second.data)
            second = second.next

        return merged_list

# Example usage
dll = DoublyLinkedList()
dll.insert_at_beginning(12)
dll.insert_at_beginning(24)
dll.insert_at_end(37)
dll.insert_at_end(49)
dll.insert_at_beginning(2)

dll_2 = DoublyLinkedList()
dll_2.insert_at_beginning(10)
dll_2.insert_at_beginning(100)
dll_2.insert_at_beginning(50)

print("Lista 1 percorrendo de frente para trás:")
dll.traverse_forward()

print("Lista 1 percorrendo de trás para frente:")
dll.traverse_backward()

dll.remove(24)
print("Lista 1 percorrendo de frente para trás após remoção de 24:")
dll.traverse_forward()

print("Lista 2 percorrendo de frente para trás:")
dll_2.traverse_forward()

print("\n")
dll_2.sort_insertion_sort()
print("Lista 2 após ordenação com Insertion Sort:")
dll_2.traverse_forward()

print("\n")
lista_mesclada = dll.merge(dll_2)
print("Lista 1 e lista 2 duplamente encadeadas ordenadas em uma única lista ordenada:")
lista_mesclada.traverse_forward()