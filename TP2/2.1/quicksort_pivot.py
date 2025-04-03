import time
import random

def partition(array, low, high, pivot_strategy):
    if pivot_strategy == "first":
        pivot_index = low
    elif pivot_strategy == "last":
        pivot_index = high
    elif pivot_strategy == "median":
        mid = (low + high) // 2
        pivot_index = mid
    else:
        raise ValueError("Choose 'first', 'last' or 'median'.")

    array[pivot_index], array[high] = array[high], array[pivot_index]
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high, pivot_strategy):
    if low < high:
        pi = partition(array, low, high, pivot_strategy)
        quickSort(array, low, pi - 1, pivot_strategy)
        quickSort(array, pi + 1, high, pivot_strategy)

def quicksort_with_pivot(array, pivot_strategy="last"):
    array_copy = array[:]
    quickSort(array_copy, 0, len(array_copy) - 1, pivot_strategy)
    return array_copy

def measure_performance():
    array_sizes = [500, 1000, 10000, 100000]
    strategies = ["first", "last", "median"]

    for size in array_sizes:
        print(f"Array size: {size}")
        array = [random.randint(1, 1000) for _ in range(size)]

        for strategy in strategies:
            start_time = time.time()
            quicksort_with_pivot(array, pivot_strategy=strategy)
            elapsed_time = time.time() - start_time
            print(f"Pivot: {strategy}, Time: {elapsed_time:.5f} s")

measure_performance()