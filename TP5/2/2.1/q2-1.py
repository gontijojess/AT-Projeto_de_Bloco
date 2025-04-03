def mochila_gulosa(capacidade, itens):
    itens.sort(key=lambda x: x['valor'] / x['peso'], reverse=True)
    
    selecionados = []
    valor_total = 0
    peso_total = 0
    
    for item in itens:
        if peso_total + item['peso'] <= capacidade:
            selecionados.append(item['nome'])
            peso_total += item['peso']
            valor_total += item['valor']
    
    return selecionados, peso_total, valor_total

itens = [
    {'nome': 'Estojo', 'peso': 2, 'valor': 40},
    {'nome': 'Carteira', 'peso': 3, 'valor': 50},
    {'nome': 'Carregador Portátil', 'peso': 5, 'valor': 100},
    {'nome': 'Casaco', 'peso': 4, 'valor': 90}
]

capacidade = 8
items, peso, valor = mochila_gulosa(capacidade, itens)

print(f"Para a capacidade da mochila de {capacidade}, os itens selecionados são:")
for item in items:
    print(item)
print(f"O peso total dos items é de {peso}")
print(f"O valor total dos items é {valor}")
