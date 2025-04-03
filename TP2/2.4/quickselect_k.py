import random

def partition(array, low, high):
    pivot_index = random.randint(low, high)
    array[pivot_index], array[high] = array[high], array[pivot_index]
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_select(array, low, high, k):
    if low == high:
        return array[low]
    pivot_index = partition(array, low, high)
    if k == pivot_index:
        return array[k]
    elif k < pivot_index:
        return quick_select(array, low, pivot_index - 1, k)
    else:
        return quick_select(array, pivot_index + 1, high, k)

def k_smallest(array, k):
    if k <= 0:
        return []
    ki = k - 1
    k_value = quick_select(array, 0, len(array) - 1, ki)
    smallest = [x for x in array if x <= k_value]
    return sorted(smallest[:k])

lista = [2, 17, 4, 8, 23, 12, 78, 21, 38, 45, 1, 16, 41]
print(f'Lista antes da ordenação: {lista}')
k = 6
k_menores_elementos = k_smallest(lista, k)
print(f'Lista parcialmente ordenada: {lista}')
print(f'Os {k} menores elementos dessa lista são {k_menores_elementos}')