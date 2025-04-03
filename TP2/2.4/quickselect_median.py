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

def find_median(array):
    n = len(array)
    if n % 2 == 1:
        return quick_select(array, 0, n - 1, n // 2)
    else:
        mid1 = quick_select(array, 0, n - 1, n // 2 - 1)
        mid2 = quick_select(array, 0, n - 1, n // 2)
        return (mid1 + mid2) / 2

lista = [2, 17, 4, 8, 23, 12, 78, 21, 38, 45, 1, 16, 41]
print(f'Lista antes da ordenação: {lista}')
mediana = find_median(lista)
print(f'Lista parcialmente ordenada: {lista}. A sua mediana é {mediana}')