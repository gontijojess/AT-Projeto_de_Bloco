import multiprocessing
import time
import math
import numpy as np

def soma_paralela(intervalo):
    return sum(intervalo)

def dividir_lista(lista, num_partes):
    tamanho_parte = len(lista) // num_partes
    return [lista[i:i + tamanho_parte] for i in range(0, len(lista), tamanho_parte)]

def exercicio_2_1():
    print("Ex 2.1) Soma Paralela de uma lista Grande:")
    lista = list(range(1, 10000001))
    num_processos = multiprocessing.cpu_count()
    partes = dividir_lista(lista, num_processos)

    with multiprocessing.Pool(num_processos) as pool:
        resultados = pool.map(soma_paralela, partes)

    soma_total = sum(resultados)
    print(f"Soma de números de 1 até 10 milhões utilizando todos os núcleos disponíveis: {soma_total}")
    print(" ")

def multiplicar_linha(args):
    matrix_A, matrix_B, linha = args
    return np.dot(matrix_A[linha,:], matrix_B)

def exercicio_2_2():
    print("Ex 2.2) Multiplicação de Matrizes com Paralelismo")
    matrix_A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix_B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    num_processos = 3  # Para 3 linhas

    with multiprocessing.Pool(num_processos) as pool:
        resultados = pool.starmap(multiplicar_linha, [(matrix_A, matrix_B, i) for i in range(len(matrix_A))])

    matriz_resultante = np.array(resultados)
    print(f"Matriz resultante da multiplicação de duas matrizes 3x3:\n{matriz_resultante}")
    print(" ")

def is_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(intervalo):
    inicio, fim = intervalo
    return sum(1 for num in range(inicio, fim) if is_primo(num))

def dividir_intervalo(inicio, fim, num_partes):
    tamanho_parte = (fim - inicio) // num_partes
    return [(inicio + i * tamanho_parte, inicio + (i + 1) * tamanho_parte) for i in range(num_partes)]

def exercicio_2_3():
    print("Ex 2.3) Paralelismo para Processamento de Tarefas Pesadas (Contagem de Primos)")
    inicio = 1
    fim = 100000
    num_processos = multiprocessing.cpu_count()
    intervalos = dividir_intervalo(inicio, fim, num_processos)

    with multiprocessing.Pool(num_processos) as pool:
        resultados = pool.map(contar_primos, intervalos)

    total_primos = sum(resultados)
    print(f"Quantidade de números primos entre 1 e 100000 utilizando todos os núcleos disponíveis: {total_primos}")
    print(" ")

def exercicio_2_4():
    print("Ex 2.4) Comparação de Desempenho")
    inicio = 1
    fim = 100000
    num_processos = multiprocessing.cpu_count()
    intervalos = dividir_intervalo(inicio, fim, num_processos)

    start = time.time()
    total_primos_sequencial = sum(contar_primos((intervalo[0], intervalo[1])) for intervalo in intervalos)
    end = time.time()
    print(f"Tempo sequencial para contagem de primos entre 1 e 100000: {end - start:.4f} segundos")

    start = time.time()
    with multiprocessing.Pool(num_processos) as pool:
        resultados = pool.map(contar_primos, intervalos)
    total_primos_paralelo = sum(resultados)
    end = time.time()
    print(f"Tempo paralelo para contagem de primos entre 1 e 100000: {end - start:.4f} segundos")
    print(" ")

if __name__ == '__main__':
    exercicio_2_1()
    exercicio_2_2()
    exercicio_2_3()
    exercicio_2_4()