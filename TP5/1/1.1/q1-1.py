class GrafoPonderado:
    def __init__(self, grafo_dict=None):
        self.vertices = grafo_dict if grafo_dict else {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self,  vertice1, vertice2, peso):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            self.vertices[vertice1].append((vertice2, peso))
            self.vertices[vertice2].append((vertice1, peso))

    def dijkstra(self, origem):
        nao_visitados = list(self.vertices.keys())
        distancias = {v: float('inf') for v in self.vertices}
        distancias[origem] = 0
        
        while nao_visitados:
            atual = min(nao_visitados, key=lambda v: distancias[v])
            
            if distancias[atual] == float('inf'):
                break
            
            for vizinho, peso in self.vertices[atual]:
                distancia_candidata = distancias[atual] + peso
                if distancia_candidata < distancias[vizinho]:
                    distancias[vizinho] = distancia_candidata
            
            nao_visitados.remove(atual)
        
        return distancias
    
# É possível criar o grafo diretamente a partir do dicionário:

# grafo = {
# 'A': [('B', 1), ('C', 4)],
# 'B': [('A', 1), ('C', 2), ('D', 5)],
# 'C': [('A', 4), ('B', 2), ('D', 1)],
# 'D': [('B', 5), ('C', 1)]
# }

# grafo = GrafoPonderado(grafo)

# OU inserindo os vértices e arestas:
        
grafo = GrafoPonderado()
vertices = ["A", "B", "C", "D"]

for vertice in vertices:
    grafo.adicionar_vertice(vertice)

arestas = [
    ("A", "B", 1), ("A", "C", 4),
    ("B", "C", 2), ("B", "D", 5),
    ("C", "E", 7), ("D", "E", 6),
    ("C", "D", 1)
]

for vertice1, vertice2, peso in arestas:
    grafo.adicionar_aresta(vertice1, vertice2, peso)

origem = "A"
distancias =grafo.dijkstra(origem)

print(f"Caminho mínimo a partir da origem '{origem}':")
for vertice, distancia in distancias.items():
    print(f"Distância até {vertice}: {distancia}")