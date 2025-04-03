def knapsack_dynamic(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

values1 = [80, 120, 170, 150]
weights1 = [5, 10, 20, 30]
capacity1 = 55
result = knapsack_dynamic(values1, weights1, capacity1)
print("Mochila 1")
print(f'Valores: {values1}')
print(f'Pesos: {weights1}')
print(f'Capacidade: {capacity1}')
print(f"O valor máximo que é possível carregar nessa mochila é {result}\n")

values2 = [1, 2, 3, 4, 5, 6]
weights2 = [6, 5, 4, 3, 2, 1]
capacity2 = 16
result = knapsack_dynamic(values2, weights2, capacity2)
print("Mochila 2")
print(f'Valores: {values2}')
print(f'Pesos: {weights2}')
print(f'Capacidade: {capacity2}')
print(f'O valor máximo que é possível carregar nessa mochila é {result}\n')

values3 = [2, 345, 67, 39, 12, 44]
weights3 = [45, 35, 12, 16, 34, 23]
capacity3 = 120
result = knapsack_dynamic(values3, weights3, capacity3)
print("Mochila 3")
print(f'Valores: {values3}')
print(f'Pesos: {weights3}')
print(f'Capacidade: {capacity3}')
print(f'O valor máximo que é possível carregar nessa mochila é {result}')