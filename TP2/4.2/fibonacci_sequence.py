import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print(f'O 1-ésimo número da sequência fibonacci é: {fibonacci_memo(1)}')
print(f'O 2-ésimo número da sequência fibonacci é: {fibonacci_memo(2)}')
print(f'O 3-ésimo número da sequência fibonacci é: {fibonacci_memo(3)}')
print(f'O 4-ésimo número da sequência fibonacci é: {fibonacci_memo(4)}')
print(f'O 5-ésimo número da sequência fibonacci é: {fibonacci_memo(5)}')
print(f'O 6-ésimo número da sequência fibonacci é: {fibonacci_memo(6)}')

start_time = time.time()
print(f'Fibonacci de 30 sem memorização: {fibonacci(30)}')
end_time = time.time()
execution_time = end_time - start_time
print(f'Tempo de execução: {execution_time:.6f} s')

start_time = time.time()
print(f'Fibonacci de 30 com memorização: {fibonacci_memo(30)}')
end_time = time.time()
execution_time = end_time - start_time
print(f'Tempo de execução: {execution_time:.6f} s')