import time
import matplotlib.pyplot as plt
import random
import numpy as np

def calcular_distancia(cidade1, cidade2):
    x1, y1 = cidade1
    x2, y2 = cidade2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5  

def encontrar_vizinho_mais_proximo(cidade_atual, cidades_nao_visitadas):
    menor_distancia = float('inf')
    cidade_mais_proxima = None
    for cidade in cidades_nao_visitadas:
        distancia = calcular_distancia(cidade_atual, cidade)
        if distancia < menor_distancia:
            menor_distancia = distancia
            cidade_mais_proxima = cidade
    return cidade_mais_proxima, menor_distancia

def tsp_vizinho_mais_proximo(cidades):
    cidade_inicial = cidades[0]
    caminho = [cidade_inicial]
    cidades_nao_visitadas = cidades[1:]
    distancia_total = 0

    cidade_atual = cidade_inicial
    while cidades_nao_visitadas:
        proxima_cidade, distancia = encontrar_vizinho_mais_proximo(cidade_atual, cidades_nao_visitadas)
        caminho.append(proxima_cidade)
        cidades_nao_visitadas.remove(proxima_cidade)
        distancia_total += distancia
        cidade_atual = proxima_cidade

    distancia_total += calcular_distancia(cidade_atual, cidade_inicial)
    caminho.append(cidade_inicial)

    return caminho, distancia_total

def generate_random_cities(n):
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

def calcular_tempo_execucao(max_cities=50, steps=5, repetitions=3):
    sizes = range(5, max_cities + 1, steps)
    execution_times = []
    distances = []
    
    for size in sizes:
        times = []
        dist = []
        for _ in range(repetitions):
            cities = generate_random_cities(size)
            
            start_time = time.time()
            path, total_distance = tsp_vizinho_mais_proximo(cities.copy())
            end_time = time.time()
            
            times.append(end_time - start_time)
            dist.append(total_distance)
        
        avg_time = sum(times) / len(times)
        avg_dist = sum(dist) / len(dist)
        execution_times.append(avg_time)
        distances.append(avg_dist)
    
    return sizes, execution_times, distances

def plot_resultados(sizes, times, distances):
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.plot(sizes, times, 'b-o')
    plt.title('Tempo de execução TSP - Vizinho mais próximo')
    plt.xlabel('Número de cidades')
    plt.ylabel('Tempo de execução (segundos)')
    plt.grid(True)
    
    plt.subplot(1, 3, 2)
    plt.plot(sizes, times, 'r-o')
    plt.yscale('log')
    plt.title('Tempo de execução TSP - Vizinho mais próximo (Escala Logarítmica)')
    plt.xlabel('Número de cidades')
    plt.ylabel('Tempo de execução (segundos)')
    plt.grid(True)
    
    plt.subplot(1, 3, 3)
    plt.plot(sizes, distances, 'g-o')
    plt.title('Distância total TSP - Vizinho mais próximo')
    plt.xlabel('Número de cidades')
    plt.ylabel('Distância total')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()


print("Testando com um exemplo pequeno:")
cidades = [(0, 0), (2, 3), (5, 4), (1, 1), (7, 2), (6, 6)]

caminho, distance = tsp_vizinho_mais_proximo(cidades.copy())

print("Melhor caminho encontrado:")
caminho_formatado = " -> ".join([str(cidade) for cidade in caminho])
print(caminho_formatado)
print(f"Total distance: {distance:.2f}")

print("\nAvaliando com diferentes tamanhos de entradas..")
sizes, times, distances = calcular_tempo_execucao(max_cities=50, steps=5)
plot_resultados(sizes, times, distances)

print("\nnEstatísticas:")
print(f"Tempo de execução mínimo: {min(times):.6f} segundos")
print(f"Tempo de execução máximo: {max(times):.6f} segundos")
print(f"Tempo de execução médio: {sum(times)/len(times):.6f} segundo")
print(f"Distância mínima: {min(distances):.2f}")
print(f"Distância máxima: {max(distances):.2f}")
print(f"Distância média: {sum(distances)/len(distances):.2f}")