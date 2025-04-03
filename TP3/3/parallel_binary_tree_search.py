import threading

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ArvoreBinaria:
    def __init__(self, raiz):
        self.raiz = raiz

    def buscar_paralelamente(self, node, valor, resultado):
        if node is None:
            return False

        if node.value == valor:
            resultado.append(node)
            return True

        found_left = threading.Event()
        found_right = threading.Event()
        left_result = []
        right_result = []

        def buscar_esquerda():
            if self.buscar_paralelamente(node.left, valor, left_result):
                found_left.set()

        def buscar_direita():
            if self.buscar_paralelamente(node.right, valor, right_result):
                found_right.set()

        t_left = threading.Thread(target=buscar_esquerda)
        t_right = threading.Thread(target=buscar_direita)

        t_left.start()
        t_right.start()

        t_left.join()
        t_right.join()

        if found_left.is_set():
            resultado.extend(left_result)
            return True
        if found_right.is_set():
            resultado.extend(right_result)
            return True
        return False

    def dfs_paralela(self, node, valor, caminho, resultado):
        if node is None:
            return False

        caminho_local = caminho + [node.value]

        if node.value == valor:
            resultado.append(list(caminho_local))
            return True

        found_left = threading.Event()
        found_right = threading.Event()
        left_result = []
        right_result = []

        def explorar_esquerda():
            if self.dfs_paralela(node.left, valor, caminho_local, left_result):
                found_left.set()

        def explorar_direita():
            if self.dfs_paralela(node.right, valor, caminho_local, right_result):
                found_right.set()

        t_left = threading.Thread(target=explorar_esquerda)
        t_right = threading.Thread(target=explorar_direita)

        t_left.start()
        t_right.start()

        t_left.join()
        t_right.join()

        if found_left.is_set():
            resultado.extend(left_result)
            return True
        if found_right.is_set():
            resultado.extend(right_result)
            return True
        return False

    def encontrar_maximo_paralelamente(self, node, max_val, resultado):
        if node is None:
            return max_val

        max_val = max(max_val, node.value)

        found_left = threading.Event()
        found_right = threading.Event()
        left_max = [max_val]
        right_max = [max_val]

        def explorar_esquerda():
            left_max[0] = self.encontrar_maximo_paralelamente(node.left, left_max[0], resultado)
            found_left.set()

        def explorar_direita():
            right_max[0] = self.encontrar_maximo_paralelamente(node.right, right_max[0], resultado)
            found_right.set()

        t_left = threading.Thread(target=explorar_esquerda)
        t_right = threading.Thread(target=explorar_direita)

        t_left.start()
        t_right.start()

        t_left.join()
        t_right.join()

        return max(left_max[0], right_max[0])

if __name__ == '__main__':
    root = Node(50)
    root.left = Node(30)
    root.right = Node(70)
    root.left.left = Node(20)
    root.left.right = Node(40)
    root.right.left = Node(60)
    root.right.right = Node(80)

    arvore = ArvoreBinaria(root)

    print("Ex 3.1) Busca Paralela em Árvore Binária")
    valor_buscado = 60
    resultado = []
    if arvore.buscar_paralelamente(root, valor_buscado, resultado):
        print(f"Valor {valor_buscado} encontrado na árvore!")
    else:
        print(f"Valor {valor_buscado} não encontrado na árvore.")
    print(" ")

    print("Ex 3.2) Busca em Profundidade (DFS) Paralela com Retorno de Caminho")
    caminho = []
    resultado = []
    valor_buscado_dfs = 40
    if arvore.dfs_paralela(root, valor_buscado_dfs, caminho, resultado):
        print(f"Caminho até o valor {valor_buscado_dfs}: {resultado[0]}")
    else:
        print(f"Valor {valor_buscado_dfs} não encontrado na árvore.")
    print(" ")

    print("Ex 3.3) Busca Paralela em Árvore para Encontrar o Valor Máximo")
    maximo = arvore.encontrar_maximo_paralelamente(root, float('-inf'), [])
    print(f"O valor máximo na árvore é: {maximo}")
    print(" ")