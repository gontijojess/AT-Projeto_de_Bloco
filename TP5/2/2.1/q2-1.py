import time
import matplotlib.pyplot as plt
import random
import copy

def mochila_gulosa(capacidade, itens):
    itens.sort(key=lambda x: x['valor'] / x['peso'], reverse=True)
    
    selecionados = []
    valor_total = 0
    peso_total = 0
    
    for item in itens:
        if peso_total + item['peso'] <= capacidade:
            selecionados.append(item['nome'])
            peso_total += item['peso']
            valor_total += item['valor']
    
    return selecionados, peso_total, valor_total

def gerar_itens_randomicos(n):
    items = []
    for i in range(n):
        items.append({
            'nome': f'Item_{i}',
            'peso': random.randint(1, 10),
            'valor': random.randint(10, 100)
        })
    return items

def calcular_tempo_execucao(max_items=100, steps=10, repetitions=5):
    sizes = range(10, max_items + 1, steps)
    execution_times = []
    
    for size in sizes:
        times = []
        for _ in range(repetitions):
            items = gerar_itens_randomicos(size)
            capacidade = size * 3
            
            start_time = time.time()
            mochila_gulosa(capacidade, copy.deepcopy(items))
            end_time = time.time()
            
            times.append(end_time - start_time)
        
        avg_time = sum(times) / len(times)
        execution_times.append(avg_time)
    
    return sizes, execution_times

def plot_resultados(sizes, times):
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(sizes, times, 'b-o')
    plt.title('Tempo de execução - Algotimo guloso')
    plt.xlabel('Quantidade de itens')
    plt.ylabel('Tempo de execução (segundos)')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(sizes, times, 'r-o')
    plt.yscale('log')
    plt.title('Tempo de Execução do Algoritmo da Mochila (Escala Logarítmica)')
    plt.xlabel('Quantidade de itens')
    plt.ylabel('Tempo de execução (segundos)')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    itens_original = [
        {'nome': 'Estojo', 'peso': 2, 'valor': 40},
        {'nome': 'Carteira', 'peso': 3, 'valor': 50},
        {'nome': 'Carregador Portátil', 'peso': 5, 'valor': 100},
        {'nome': 'Casaco', 'peso': 4, 'valor': 90}
    ]
    
    capacidade = 8
    items, peso, valor = mochila_gulosa(capacidade, copy.deepcopy(itens_original))
    print(f"Para a capacidade da mochila de {capacidade}, os itens selecionados são:")
    print(f"Itens selecionados: {items}")
    print(f"Peso total: {peso}")
    print(f"Valor total dos itens: {valor}")
    
    print("\nCalculando a performance:")
    sizes, times = calcular_tempo_execucao(max_items=1000, steps=50)
    plot_resultados(sizes, times)
    
    print("\nEstatísticas")
    print(f"Tempo de execução mínimo: {min(times):.6f} segundos")
    print(f"Tempo de execução máximo: {max(times):.6f} segundos")
    print(f"Tempo de execução médio: {sum(times)/len(times):.6f} segundo")