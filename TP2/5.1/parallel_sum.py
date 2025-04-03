from multiprocessing import Pool, cpu_count
import time

def sum_parallel(lst, n_threads):
    with Pool(n_threads) as pool:
        chunk_size = (len(lst) + n_threads - 1) // n_threads
        chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
        results = pool.map(sum, chunks)
        return sum(results)

def sum_sequential(lst):
    return sum(lst)

if __name__ == "__main__":
    large_list = list(range(1, 1000000))
    n_threads = cpu_count()

    print(f"Quantidade de threads: {n_threads}")
    print(f"Tamanho da lista: {len(large_list)}")

    start_time = time.time()
    parallel_total = sum_parallel(large_list, n_threads)
    end_time = time.time()
    parallel_time = end_time - start_time
    print("\nSoma Paralela:")
    print(f"Tempo de execução: {parallel_time:.4f} segundos")
    print(f"Total da soma: {parallel_total}")

    start_time = time.time()
    sequential_total = sum_sequential(large_list)
    end_time = time.time()
    sequential_time = end_time - start_time
    print("\nSoma Sequencial:")
    print(f"Tempo de execução: {sequential_time:.4f} segundos")
    print(f"Total da soma: {sequential_total}")