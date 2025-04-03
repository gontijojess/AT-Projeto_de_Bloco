import time
import psutil
import os
import pandas as pd

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]
        self.size = 0
    
    def hash(self, key):
        return hash(key) % self.capacity
    
    def insert(self, key, value):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        self.size += 1
    
    def search(self, key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def remove(self, key):
        index = self.hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                self.size -= 1
                return True
        return False
    
    def __str__(self):
        result = []
        for bucket in self.table:
            for pair in bucket:
                result.append(f"{pair[0]}: {pair[1]}")
        return "{" + ", ".join(result) + "}"

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Empty stack"
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print("Stack", self.items)
    
    def find_file(self, index):
        temp_stack = Stack()
        index_n = self.size() - index
        found_item = None
        for i in range(index_n):
            found_item = self.pop()
            temp_stack.push(found_item)
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
        return found_item
    
    def remove_by_position(self, position):
        temp_stack = Stack()
        convert_index = self.size() - position - 1
        removed_item = None
        for i in range(self.size()):
            item = self.pop()
            if i == convert_index:
                removed_item = item
                break
            temp_stack.push(item)
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())
        return removed_item

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            print("Empty queue")
            return None
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
            print("Empty queue")
            return None
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("Empty queue")
        else:
            print("Queue", end=" ")
            for item in self.items:
                print(item, end=" ")
            print()
    
    def find_file(self, index):
        found_item = None
        for i in range(self.size()):
            item_row = self.dequeue()
            if i == index:
                found_item = item_row
            self.enqueue(item_row)
        return found_item
    
    def remove_by_position(self, position):
        temp_queue = Queue()
        removed_item = None
        for i in range(self.size()):
            item_row = self.dequeue()
            if i == position:
                removed_item = item_row
            else:
                temp_queue.enqueue(item_row)
        return removed_item

def read_file(filename):
    with open(filename, 'r') as file:
        file_list = [row.strip() for row in file.readlines()]
    return file_list

file_tp1 = 'lista_tp1.txt'
list_tp1 = read_file(file_tp1)

new_hashtable = list_to_hashtable(list_tp1)
new_hashtable_copy = list_to_hashtable(list_tp1)
new_stack = list_to_stack(list_tp1)
new_stack_copy = list_to_stack(list_tp1)
new_queue = list_to_queue(list_tp1)
new_queue_copy = list_to_queue(list_tp1)
test_queue = list_to_queue(list_tp1)

print("Search for items:")
print("Hash:")
start_time = time.time()
result = new_hashtable.search(1)
end_time = time.time()
print(f"File: {result} - position 1 - time: {end_time - start_time}")

start_time = time.time()
result = new_hashtable.search(100)
end_time = time.time()
print(f"File: {result} - position 100 - time: {end_time - start_time}")

start_time = time.time()
result = new_hashtable.search(1000)
end_time = time.time()
print(f"File: {result} - position 1000 - time: {end_time - start_time}")

start_time = time.time()
result = new_hashtable.search(5000)
end_time = time.time()
print(f"File: {result} - position 5000 - time: {end_time - start_time}")

start_time = time.time()
result = new_hashtable.search(new_hashtable.size - 1)
end_time = time.time()
print(f"File: {result} - last position - time: {end_time - start_time}")

print("\nStack:")
start_time = time.time()
result = new_stack.find_file(1)
end_time = time.time()
print(f"File: {result} - position 1 - time: {end_time - start_time}")

start_time = time.time()
result = new_stack.find_file(100)
end_time = time.time()
print(f"File: {result} - position 100 - time: {end_time - start_time}")

start_time = time.time()
result = new_stack.find_file(1000)
end_time = time.time()
print(f"File: {result} - position 1000 - time: {end_time - start_time}")

start_time = time.time()
result = new_stack.find_file(5000)
end_time = time.time()
print(f"File: {result} - position 5000 - time: {end_time - start_time}")

start_time = time.time()
result = new_stack.find_file(new_hashtable.size - 1)
end_time = time.time()
print(f"File: {result} - last position - time: {end_time - start_time}")

print("\nQueue:")
start_time = time.time()
result = new_queue.find_file(1)
end_time = time.time()
print(f"File: {result} - position 1 - time: {end_time - start_time}")

start_time = time.time()
result = new_queue.find_file(100)
end_time = time.time()
print(f"File: {result} - position 100 - time: {end_time - start_time}")

start_time = time.time()
result = new_queue.find_file(1000)
end_time = time.time()
print(f"File: {result} - position 1000 - time: {end_time - start_time}")

start_time = time.time()
result = new_queue.find_file(5000)
end_time = time.time()
print(f"File: {result} - position 5000 - time: {end_time - start_time}")

start_time = time.time()
result = new_queue.find_file(new_queue.size() - 1)
end_time = time.time()
print(f"File: {result} - last position - time: {end_time - start_time}")

try:
    excel_path = "Operacoes de inserçao e remoção.xlsx"
    df = pd.read_excel(excel_path)

    insercao = dict(zip(df.iloc[0:, 0], df.iloc[0:, 2]))
    remocao = df.iloc[0:, 5].tolist()

    print("\nRemove and save items")
    print("Hash:")
    start_time = time.time()
    for key, value in insercao.items():
        new_hashtable.insert(key, value)
    end_time = time.time()
    print(f"Time to insert from list: {end_time - start_time}")

    start_time = time.time()
    for x in remocao:
        new_hashtable.remove(x)
    end_time = time.time()
    print(f"Time to remove from list: {end_time - start_time}")

    print("\nStack:")
    start_time = time.time()
    for key, value in insercao.items():
        new_stack.push(value)
    end_time = time.time()
    print(f"Time to insert from list: {end_time - start_time}")

    start_time = time.time()
    for x in remocao:
        new_stack.remove_by_position(x)
    end_time = time.time()
    print(f"Time to remove from list: {end_time - start_time}")

    print("\nQueue:")
    start_time = time.time()
    for key, value in insercao.items():
        new_queue.enqueue(value)
    end_time = time.time()
    print(f"Time to insert from list: {end_time - start_time}")

    start_time = time.time()
    for x in remocao:
        new_queue.remove_by_position(x)
    end_time = time.time()
    print(f"Time to remove from list: {end_time - start_time}")

except Exception as e:
    print(f"\nError processing Excel file: {e}")