class GrafoPrim:
    def __init__(self, grafo_dict=None):
        self.vertices = grafo_dict if grafo_dict else {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self,  vertice1, vertice2, peso):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].append((vertice2, peso))
            self.vertices[vertice2].append((vertice1, peso))

    def prim(self, inicio):
        if inicio not in self.vertices:
            return {}

        infinito = float('inf')
        vertices = list(self.vertices.keys())
        num_vertices = len(vertices)
        indice = {v: i for i, v in enumerate(vertices)}
        
        selecionado = [False] * num_vertices
        chave = [infinito] * num_vertices
        pai = [None] * num_vertices

        chave[indice[inicio]] = 0

        for _ in range(num_vertices):
            u = -1
            min_chave = infinito
            for v in range(num_vertices):
                if not selecionado[v] and chave[v] < min_chave:
                    min_chave = chave[v]
                    u = v

            if u == -1:
                break

            selecionado[u] = True

            for vizinho, peso in self.vertices[vertices[u]]:
                v = indice[vizinho]
                if not selecionado[v] and peso < chave[v]:
                    chave[v] = peso
                    pai[v] = u

        mst_arestas = []
        for i in range(num_vertices):
            if pai[i] is not None:
                mst_arestas.append((
                    vertices[pai[i]], 
                    vertices[i], 
                    chave[i]
                ))

        return mst_arestas
    
# É possível criar o grafo diretamente a partir do dicionário:

# grafo = {
# 'A': [('B', 2), ('C', 3)],
# 'B': [('A', 2), ('C', 1), ('D', 4)],
# 'C': [('A', 3), ('B', 1), ('D', 5)],
# 'D': [('B', 4), ('C', 5)]
# }

# grafo = GrafoPonderado(grafo)

# OU inserindo os vértices e arestas:
        
grafo = GrafoPrim()
vertices = ["A", "B", "C", "D"]

for vertice in vertices:
    grafo.adicionar_vertice(vertice)

arestas = [
    ("A", "B", 2), ("A", "C", 3),
    ("B", "C", 1), ("B", "D", 4),
    ("C", "D", 5)
]

for vertice1, vertice2, peso in arestas:
    grafo.adicionar_aresta(vertice1, vertice2, peso)

inicio = 'A'
mst = grafo.prim(inicio)

print(f"\nÁrvore Geradora Mínima a partir do vértice {inicio}:")
peso_total = 0
for aresta in mst:
    print(f"{aresta[0]} - {aresta[1]} com peso {aresta[2]}")
    peso_total += aresta[2]