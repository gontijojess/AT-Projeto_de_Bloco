import time
import matplotlib.pyplot as plt

def hanoi(disc, ori, dest, aux):
    if disc == 1:
        return
    hanoi(disc - 1, ori, aux, dest)
    hanoi(disc - 1, aux, dest, ori)

def measure_hanoi_time_complexity():
    discs = list(range(1, 31))
    time_list = []

    for n in discs:
        start_time = time.time()
        hanoi(n, 'A', 'C', 'B')
        end_time = time.time()
        execution_time = end_time - start_time
        time_list.append(execution_time)
        print(f"O tempo para {n} discos é de {execution_time:.6f} segundos")

    plt.plot(discs, time_list, marker='o', linestyle='-', color='b')
    plt.xlabel('Número de Discos')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Tempo de Execução das Torres de Hanói')
    plt.savefig('grafico_hanoi.png')
    print('Grafico salvo como grafico_hanoi.png')

measure_hanoi_time_complexity()