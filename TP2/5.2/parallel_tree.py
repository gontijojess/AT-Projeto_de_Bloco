from multiprocessing import Process, Value
import time

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_subtree(node, target, found):
    if node is None or found.value:
        return
    if node.value == target:
        found.value = True
        return
    search_subtree(node.left, target, found)
    search_subtree(node.right, target, found)

def parallel_search(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    found = Value('b', False)
    left_proc = Process(target=search_subtree, args=(root.left, target, found))
    right_proc = Process(target=search_subtree, args=(root.right, target, found))

    left_proc.start()
    right_proc.start()
    left_proc.join()
    right_proc.join()
    return found.value

def add_node(root, value):
    if value < root.value:
        if root.left is None:
            root.left = TreeNode(value)
        else:
            add_node(root.left, value)
    else:
        if root.right is None:
            root.right = TreeNode(value)
        else:
            add_node(root.right, value)

def build_tree(values):
    root = TreeNode(values[0])
    for value in values[1:]:
        add_node(root, value)
    return root

def measure_time(n):
    values = list(range(n))
    target = n - 1
    root = build_tree(values)
    start_time = time.time()
    found = parallel_search(root, target)
    elapsed_time = time.time() - start_time
    return elapsed_time, found

if __name__ == "__main__":
    for i in range(0, 9):
        n = 2 ** i
        print(f"\nÁrvore com {n} nós:")
        time_taken, found = measure_time(n)
        print(f"Encontrado? {'Sim' if found else 'Não'}")
        print(f"Tempo de execução: {time_taken:.6f} segundos")