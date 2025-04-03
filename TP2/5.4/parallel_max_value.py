import random
import time
import multiprocessing

def max_value(lst):
    return max(lst)

def max_parallel(lst):
    num_processes = multiprocessing.cpu_count()
    chunk_size = len(lst) // num_processes
    chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
    with multiprocessing.Pool(processes=num_processes) as pool:
        local_maxes = pool.map(max_value, chunks)
    return max(local_maxes)

if __name__ == '__main__':
    size = 100000
    random_list = [random.randint(0, 1000000) for _ in range(size)]

    start_time = time.time()
    seq_max = max_value(random_list)
    seq_time = time.time() - start_time
    print(f"Encontrar valor máximo ({seq_max}) versão sequencial:")
    print(f"Tempo: {seq_time:.6f} s")

    start_time = time.time()
    par_max = max_parallel(random_list)
    par_time = time.time() - start_time
    print(f"\nEncontrar valor máximo ({par_max}) versão paralela:")
    print(f"Tempo: {par_time:.6f} s")