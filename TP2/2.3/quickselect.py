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

def generate_random_array(size=10000, min_val=1, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(size)]

for i in range(10):
    lista = generate_random_array()
    print(f"Lista {i + 1}:")
    for k in [1, 500, 1000, 5000, 9000]:
        k_1 = k - 1
        result = quick_select(lista, 0, len(lista) - 1, k_1)
        print(f"{k}-ésimo menor elemento: {result}")
    print("---")