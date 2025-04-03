def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    coins_results = [[] for _ in range(amount + 1)]
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coins_results[i] = coins_results[i - coin] + [coin]
    
    if dp[amount] == amount + 1:
        return []
    return coins_results[amount]

coins = [5, 10, 25, 50]
amount = 140

used_coins = coin_change(coins, amount)
min_num = len(used_coins)
print(f"Quantidade mínima de moedas para {amount}: {min_num}")

if min_num > 0:
    print(f"Moedas utilizadas: {used_coins}")
else:
    print("Não foi possível alcançar o valor definido com as moedas disponíveis.")