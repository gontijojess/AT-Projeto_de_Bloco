import random
import time
from multiprocessing import Pool

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_sequential(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_sequential(arr[:mid])
    right = merge_sort_sequential(arr[mid:])
    return merge(left, right)

def merge_sort_parallel(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    with Pool(2) as pool:
        left, right = pool.map(merge_sort_sequential, [arr[:mid], arr[mid:]])
    return merge(left, right)

if __name__ == "__main__":
    random_arr = [random.randint(0, 10000) for _ in range(10000)]

    start_time = time.time()
    merge_sort_sequential(random_arr)
    end_time = time.time()
    sequential_time = end_time - start_time
    print("MergeSort sequential:")
    print(f"Tempo de execução: {sequential_time:.6f} s")

    start_time = time.time()
    merge_sort_parallel(random_arr)
    end_time = time.time()
    parallel_time = end_time - start_time
    print("\nMergeSort paralelo:")
    print(f"Tempo de execução: {parallel_time:.6f} s")