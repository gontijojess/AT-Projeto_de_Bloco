import time

def ler_arquivo(arquivo):
    with open(arquivo, 'r') as file:
        arquivos = [linha.strip() for linha in file.readlines()]
    return arquivos

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

def insert_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i-1
        while j >= 0 and key < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = key

lista_arquivos = 'lista_tp1.txt'
arquivos = ler_arquivo(lista_arquivos)
arquivos_bubble = arquivos[:]
arquivos_selection = arquivos[:]
arquivos_insertion = arquivos[:]

start_time = time.time()
bubble_sort(arquivos_bubble)
end_time = time.time()
total_time_b = end_time - start_time

start_time = time.time()
selection_sort(arquivos_selection)
end_time = time.time()
total_time_s = end_time - start_time

start_time = time.time()
insert_sort(arquivos_insertion)
end_time = time.time()
total_time_i = end_time - start_time

print(f'Tempo de execução Bubble Sort: {total_time_b:.5f} segundos')
print(f'Tempo de execução Selection Sort: {total_time_s:.5f} segundos')
print(f'Tempo de execução Insert Sort: {total_time_i:.5f} segundos')