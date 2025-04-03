def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

print(f'Fatorial de 2: {fatorial(2)}')
print(f'Fatorial de 10: {fatorial(10)}')
print(f'Fatorial de 50: {fatorial(50)}')
print(f'Fatorial de 100: {fatorial(100)}')