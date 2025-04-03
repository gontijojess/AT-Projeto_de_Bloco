import time

def ip_to_int_list(ip):
    return list(map(int, ip.split('.')))

def busca_linear(prefixos, ip):
    ip_int = ip_to_int_list(ip)
    melhor_prefixo = None
    melhor_comprimento = 0

    for prefixo in prefixos:
        prefixo_ip = prefixo.split('/')[0]
        prefixo_int = ip_to_int_list(prefixo_ip)
        comprimento = len(prefixo_int)
        if ip_int[:comprimento] == prefixo_int and comprimento > melhor_comprimento:
            melhor_prefixo = prefixo
            melhor_comprimento = comprimento

    return melhor_prefixo

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_prefix = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, prefixo):
        node = self.root
        for parte in ip_to_int_list(prefixo.split('/')[0]):
            if parte not in node.children:
                node.children[parte] = TrieNode()
            node = node.children[parte]
        node.is_end_of_prefix = True

    def search_longest_prefix(self, ip):
        node = self.root
        melhor_prefixo = None
        ip_int = ip_to_int_list(ip)
        prefixo_atual = []

        for parte in ip_int:
            if parte not in node.children:
                break
            node = node.children[parte]
            prefixo_atual.append(str(parte))
            if node.is_end_of_prefix:
                melhor_prefixo = '.'.join(prefixo_atual)

        return melhor_prefixo

def gerar_prefixos(n):
    prefixos = []
    for i in range(n):
        prefixo = f"{i//256}.{(i%256)//16}.{(i%16)}.0/(24 if i%2 == 0 else 16)"
        prefixos.append(prefixo)
    return prefixos

prefixos = gerar_prefixos(1000)
ip = "192.168.1.55"

inicio = time.time()
resultado_linear = busca_linear(prefixos, ip)
tempo_linear = time.time() - inicio

trie = Trie()
for prefixo in prefixos:
    trie.insert(prefixo.split('/')[0])

inicio = time.time()
resultado_trie = trie.search_longest_prefix(ip)
tempo_trie = time.time() - inicio

print(f"Busca Linear: Prefixo mais longo = {resultado_linear}, Tempo = {tempo_linear:.6f} segundos")
print(f"Trie: Prefixo mais longo = {resultado_trie}, Tempo = {tempo_trie:.6f} segundos")