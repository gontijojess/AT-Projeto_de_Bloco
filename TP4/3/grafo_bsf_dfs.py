class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)

    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            print(f"{vertice} -> {self.lista_adjacencia[vertice]}")

    def dfs(self, inicio):
        visitados = set()
        ordem_visita = []

        def _dfs_recursivo(vertice):
            if vertice not in visitados:
                visitados.add(vertice)
                ordem_visita.append(vertice)
                for vizinho in self.lista_adjacencia[vertice]:
                    _dfs_recursivo(vizinho)

        _dfs_recursivo(inicio)
        return ordem_visita

    def bfs(self, inicio):
        visitados = set()
        fila = [inicio]
        ordem_visita = []

        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                visitados.add(vertice)
                ordem_visita.append(vertice)
                fila.extend(self.lista_adjacencia[vertice])

        return ordem_visita

    def encontrar_caminho(self, inicio, fim):
        visitados = set()
        fila = [(inicio, [inicio])]

        while fila:
            vertice, caminho = fila.pop(0)
            if vertice == fim:
                return caminho
            if vertice not in visitados:
                visitados.add(vertice)
                for vizinho in self.lista_adjacencia[vertice]:
                    fila.append((vizinho, caminho + [vizinho]))

        return None

    def mostrar_caminho(self, caminho):
        if not caminho:
            return "Caminho não encontrado."

        mostrar_caminho = ""
        for i in range(len(caminho)):
            mostrar_caminho += f"{caminho[i]}"
            if i < len(caminho) - 1:
                mostrar_caminho += " -> "
        return mostrar_caminho

grafo = Grafo()

print("Exercício 3.1 – Representação de grafo (lista de adjacência):")
vertices = ["A", "B", "C", "D", "E"]
for v in vertices:
    grafo.adicionar_vertice(v)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E"), ("H", "I")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)
print("Lista de Adjacência do Grafo:")
grafo.mostrar_grafo()
print()

print("Exercício 3.2 – DFS em grafo:")
ordem_dfs = grafo.dfs("A")
print("Ordem de visita usando DFS:")
print(grafo.mostrar_caminho(ordem_dfs))
print()

print("Exercício 3.3 – BFS em grafo:")
ordem_bfs = grafo.bfs("A")
print("Ordem de visita usando BFS:")
print(grafo.mostrar_caminho(ordem_bfs))
print()

print("Exercício 3.4 – Busca de caminho entre dois nós:")
inicio = "A"
fim = "E"
caminho = grafo.encontrar_caminho(inicio, fim)
print(f"Caminho de {inicio} até {fim}:")
print(grafo.mostrar_caminho(caminho))