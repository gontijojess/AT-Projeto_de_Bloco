import numpy as np
from parallel_x_sequential import parallel_sum, sequential_sum
from time import time

np.random.seed(42)
vector = np.random.randint(1, 100001, size=10000).astype(np.float64)

start_time = time()
sequential_result = sequential_sum(vector)
end_time = time()
sequential_time = end_time - start_time

start_time = time()
parallel_result = parallel_sum(vector)
end_time = time()
parallel_time = end_time - start_time

print(f"Tempo de execução da soma sequencial: {sequential_time:.6f} segundos")
print(f"Tempo de execução da soma paralela: {parallel_time:.6f} segundos")
print(f"Resultado sequencial: {sequential_result}")
print(f"Resultado paralelo: {parallel_result}")
print(f"Diferença: {abs(parallel_result - sequential_result)}")