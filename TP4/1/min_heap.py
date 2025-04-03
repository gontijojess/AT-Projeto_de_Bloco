class MinHeap:
    def __init__(self):
        self.heap = []

    def criar_heap(self, lista):
        self.heap = lista.copy()
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify(i, len(self.heap))

    def exibir_heap(self):
        return self.heap

    def inserir(self, valor):
        self.heap.append(valor)
        indice = len(self.heap) - 1
        while indice > 0:
            pai = (indice - 1) // 2
            if self.heap[indice] < self.heap[pai]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def remover_primeiro(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify(0, len(self.heap))
        return root

    def _heapify(self, indice, tamanho):
        menor = indice
        esq = 2 * indice + 1
        dir = 2 * indice + 2

        if esq < tamanho and self.heap[esq] < self.heap[menor]:
            menor = esq
        if dir < tamanho and self.heap[dir] < self.heap[menor]:
            menor = dir

        if menor != indice:
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            self._heapify(menor, tamanho)

    def buscar_heap(self, valor):
        return valor in self.heap

lista_int = [5, 11, 3, 7, 1, 2, 9]
heap = MinHeap()

heap.criar_heap(lista_int)
print("Exercício 1.1 - Implementar criação e leitura de heap:")
print("Heap criada:", heap.exibir_heap())
print()

print("Exercício 1.2 - Inserir elemento na heap:")
new_element = 0
print(f"Inserindo o novo elemento '{new_element}' ...")
print("Heap antes da inserção:", heap.exibir_heap())
heap.inserir(new_element)
print("Heap após a inserção:", heap.exibir_heap())
print()

print("Exercício 1.3 - Buscar elemento na heap:")
print("Buscando elemento 8 na heap:", heap.buscar_heap(8)) 
print("Buscando elemento 2 na heap:", heap.buscar_heap(2))
print()

print("Exercício 1.4 – Remoção do menor elemento:")
print("Heap antes da remoção:", heap.exibir_heap())
menor = heap.remover_primeiro()
print("Elemento removido:", menor)
print("Heap após a remoção:", heap.exibir_heap())